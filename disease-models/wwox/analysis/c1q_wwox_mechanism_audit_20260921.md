# C1q → WWOX mechanism audit — PMID 19484134 (Hong et al. 2009), `FT-108`

**Actor:** Scientist A · **Date:** 2026-09-20 (file dated 20260921 per task) · **Mode:** READ-ONLY toward every canonical file. **No commit candidate. No canonical edit. No therapy proposed, no drug or drug class named.**

Source: PubMed / PMC. According to PubMed, the article is Hong Q, Sze C-I, Lin S-R, Lee M-H, He R-Y, Schultz L, Chang J-Y, Chen S-J, Boackle RJ, Hsu L-J, Chang N-S. "Complement C1q activates tumor suppressor WWOX to induce apoptosis in prostate cancer cells." *PLoS One* 2009;4(6):e5755. [DOI](https://doi.org/10.1371/journal.pone.0005755)

---

## 0 · Header — declared read depth and surface integrity

| Field | Value |
|---|---|
| **Declared read depth** | ✅ **FULL BODY READ.** Introduction, Results (all 8 result sections), Discussion, Materials and Methods, and all figure legends (Figures 1–10) plus four Supporting-Information legends (S1–S4) were delivered as text and read end to end. |
| **Body obtainable?** | **Yes.** `get_full_text_article(pmc_ids=["PMC2685983"])` returned a populated `full_text` on the first call. |
| **Licence** | `get_copyright_status(["19484134"])` → `"license": {"type": "CC BY 4.0", "is_open_access": true}`, `source: "pmc"`, `open_access_count: 1`. Genuinely open access. The `FT-108` queue entry is correct on this point. |
| **Gene symbols survived extraction?** | ⚠️ **PARTIALLY — and the failure mode is specific and must be stated.** Protein-name usage survived intact and legible: `WWOX`, `WOX1`, `WOX2`, `hWOX1`, `p-WOX1`, `C1q`, `C6`, `C9`, `p53`, `JNK1`, `ERK`, `STAT3`, `Hyal-2` all present many times. **But every *italicised* token was silently deleted**, and in this paper the italicised tokens include the *gene* symbol. See § 0a. This is **not** the total-stripping failure of `PMID 41153369`; it is selective italic deletion. |
| **Tables obtainable?** | **Not applicable** — this paper contains no tables. Nothing was lost on that axis. |
| **Figures** | 🔴 **No figure images. No PDF tooling.** I have the **legends** of Figures 1–10 and S1–S4 as text, and the Results prose. **I did not inspect a single panel and make no claim about one.** Every statement below about what a figure "shows" is a statement about what the legend or the prose *asserts*, never about pixels. |
| **Statistics recoverable?** | ⚠️ Partially. The italic-stripping deleted the italic *P* from every p-value, leaving bare `<0.001` / `<0.0001` strings, and deleted the italic *t* from "Student's *t* test" (delivered as "Student's test"). The numeric thresholds survived; the symbol did not. I restore `P` below **in square brackets** and never silently. |

### 0a · Exactly what the extractor deleted (verified, load-bearing)

Deleted italic tokens, reconstructed from context and flagged as reconstruction, **never as delivered text**:

| Delivered string | Almost certainly | Evidence |
|---|---|---|
| "alterations of human␣gene occur most frequently in prostate and breast" | *WWOX* (gene, italic) | grammar requires a gene name |
| "Human tumor suppressor gene␣encodes the mRNA for translating into WWOX/WOX1, WOX2" | *WWOX* (gene, italic) | ditto |
| "C1q and C6 are likely to support alternatively splicing of␣mRNA" | *WWOX* (gene, italic) | ditto |
| "composed of two␣-terminal WW domains … and a␣-terminal short-chain alcohol dehydrogenase/reductase (SDR) domain" | *N*-terminal … *C*-terminal | known WWOX architecture |
| "its apoptotic activity both␣and␣–" | *in vitro* and *in vivo* | standard phrasing |
| "`<0.001`", "`<0.0001`" | *P*<0.001 etc. | italic *P* |
| "Student's␣test" | Student's *t* test | italic *t* |

🔴 **Consequence for this audit:** the N-terminal / C-terminal distinction is **reconstructed, not read**. Wherever the domain architecture matters below I say so. **I never infer which protein a sentence refers to** — in every sentence I quote, the protein is named in roman type and survived.

⚠️ **Second deletion class:** inline figure *cross-references* were also stripped, leaving empty parentheses — e.g. "rapidly induced accumulation of p-WOX1 in the nuclei ()." So **I cannot map a given Results sentence to a numbered panel.** The legends are intact and numbered; the pointers from prose to legend are gone. Where I pair a sentence with a figure below, that pairing is **my inference from section order and legend content**, and is marked.

---

## 1 · Identifier verification (performed first, independently)

`get_article_metadata(["19484134"])` and `convert_article_ids(["19484134"])` return concordantly:

- **PMID** 19484134 · **PMCID** PMC2685983 · **DOI** 10.1371/journal.pone.0005755
- *PLoS One* 2009;4(6):e5755, published 2009-06-01
- **Last author: Chang, Nan-Shan.** ✅ The Chang-lab flag applies.

✅ PMID, PMCID and DOI in the task brief and in `FT-108` are all correct.

### 🔴 Two repository records are wrong — both are pointers, neither is a scientific claim

**(a) The registry wikilink in `FT-108` points at the wrong paper.** `FT-108` states the paper "esiste come `[[paper_registry_current#CORPUS P331]]`", and the task brief repeats "sits in the registry as **CORPUS P331**". It does not. Verified by reading the registry:

- `## CORPUS P330` — "Complement C1q activates tumor suppressor WWOX to induce apoptosis in prostat…", **Authors: Hong et al.**, Year 2009, PLoS One, `Identifier: PMID 19484134 / PMC2685983 / DOI 10.1371/journal.pone.0005755`, `Tier (FASE 1): C`, `Status: screened — corpus placeholder`, `LIT link: LIT-0330`, `Claim links: none — triage only`, `Role: background corpus only`, `Note: FASE 1 triage 221–400 — no deep-dive performed`.
- `## CORPUS P331` — **a different paper entirely**: "Virus-encoded miR-155 ortholog in Marek's disease virus promotes cell proliferation via suppressing apoptosis by targeting tumor suppressor WWOX", Zhu et al. 2021, *Vet Microbiol*, PMID 33191002.

The **substantive** claim in `FT-108` — that LEGEND holds this paper at triage depth only, with no deep-dive and no claim links — is **confirmed correct against P330**. Only the ID is wrong. The companion audit `c1q_wwox_activation_audit_20260921.md` § 3 inherited the same wrong ID. **Not edited (read-only); recorded for repair.**

**(b) The first author is wrong in both the queue and the task brief.** Both say "Hsu L-J, … Chang N-S 2009". PubMed gives the author list as **Hong Q** (first), … **Hsu L-J** (tenth), **Chang N-S** (eleventh/last). Hsu Li-Jin is the *penultimate* author, not the first. The registry entry `CORPUS P330` has it right ("Hong et al."). Minor, but this paper should be cited as **Hong 2009**, not Hsu 2009.

---

## 2 · Question 1 — What is "activation", measured?

### 2.1 The abstract sentence is verbatim-confirmed, and the body is narrower than it

The task's premise sentence is **exactly correct as an abstract quote**:

> "Exogenous C1q rapidly restored the WOX1 activation (with Tyr33 phosphorylation) in less than 2 hr."

The Discussion restates it:

> "C1q rapidly induces accumulation of activated WOX1 in the nuclei in non-transfected DU145 cells in less than 2 hr. Without serum C1q or C6, the nuclear accumulation is blocked. However, WOX1 nuclear accumulation can be restored by exogenous C1q."

⚠️ **Note what the Discussion sentence actually says the measured quantity is: *nuclear accumulation*, not phosphorylation.** The abstract's parenthesis "(with Tyr33 phosphorylation)" describes the *epitope of the antibody*, not a separately measured phospho-signal in that experiment.

### 2.2 The assay: immunofluorescence localisation, plus a Western blot — no FRET

**Assay 1 — immunofluorescence microscopy (the "restoration" experiment).** Results, verbatim:

> "Human DU145 cells were cultured overnight in the presence of heat-inactivated fetal bovine serum (10%), followed by starvation for 1 hr without serum. These cells were then treated with purified C1q for 1 hr. Localization of p-WOX1 was determined by immunofluorescence microscopy. These starved cells had very low levels of cytoplasmic p-WOX1 (). Exogenous C1q rapidly induced accumulation of p-WOX1 in the nuclei (). In comparison, when the starved cells were cultured in 1% C1q-depleted (ΔC1q) human serum for 1 hr, p-WOX1 was mainly localized in the cytoplasm (). Reconstitution of ΔC1q serum with purified C1q rapidly induced p-WOX1 accumulation in the nuclei ()."

Figure 1 legend, verbatim:

> "(A,B) DU145 cells were grown on cover glass and cultured overnight in 10% heat-inactivated fetal bovine serum. The cells were then starved under serum-free conditions for 1 hr, followed by treating with or without purified C1q (1 µg/ml) for 1 hr. Localization of **endogenous** Tyr33-phosphorylated WOX1 (p-WOX1) was determined by immunofluorescence microscopy. (C,D) In addition, the starved cells were then cultured in 1% C1q-depleted human serum (ΔC1q serum) for 1 hr, in the presence or absence of exogenous C1q (1 µg/ml). (E) Presence of p-WOX1 in the nuclei is shown from counting ∼100 cells in 3 experiments (mean±standard deviation)." *(emphasis mine)*

**So the add-back experiment exists and it is on endogenous protein.** The quantified readout is **the number of cells out of ~100 scoring p-WOX1 in the nucleus**, n=3. **No p-value is stated in the Figure 1 legend.**

**Assay 2 — Western blot (the depletion experiment).** Figure 8 legend, verbatim:

> "(F) Again, identical experiments were carried out for Western blotting. Under C1q-free conditions (ΔC1q serum), the basal activation of WOX1 was significantly reduced (∼50% reduction; [P]<0.001 from versus SF and NHS; Student's [t] test; n = 3)."

And in Results:

> "Additionally, when DU145 cells were cultured in serum without C1q or C6, the levels of p-WOX1 were significantly decreased in DU145 cells, compared with other culture conditions, as determined by immunofluorescence microscopy (). These observations were further confirmed by Western blotting, which revealed downregulation of p-WOX1 under C1q-free conditions (). Under these conditions, p-WOX1 was present mainly in the cytoplasm of DU145 cells."

✅ **This is the strongest quantitative activation datum in the paper: ~50% reduction of basal p-WOX1 by Western blot under C1q depletion, [P]<0.001, n=3, on endogenous protein.**

**No FRET anywhere.** TIRF microscopy is used, but for membrane/microvillus morphology of EGFP-WOX1, not for activation.

### 2.3 The antibody — in-house, and the one validation that matters is absent

Methods, verbatim:

> "Specific antibodies against WOX1, WOX2, and its Tyr33-phosphorylated form (p-WOX1) were produced in rabbits, as described–."

🔴 **This is an in-house rabbit polyclonal, referenced to prior Chang-lab work, with no catalogue number, no lot, and — critically — no specificity control reported in this paper.** The paper has a Y33R mutant in hand. **It never blots or stains Y33R with the p-WOX1 antibody.** That single experiment would have made "pY33" a residue-level measurement; it was not done, or at least is not reported. The only negative controls described are secondary-antibody-only:

> "In negative controls, cells were stained with secondary antibody only. The resulting background fluorescence was used to subtract the positive signals…"

A secondary-only control tests secondary-antibody background. **It does not test whether the primary antibody's signal requires Tyr33.**

### 2.4 Timecourse

There is **no kinetic series** for activation. Every activation experiment is a **single fixed endpoint**:

- IF add-back: **1 hr** C1q (1 µg/ml), per Figure 1 legend.
- Depletion Western/IF: **16–24 hr** in complement-depleted serum ("cultured overnight"; Methods: "for 16–24 hr").

The abstract's "in less than 2 hr" and the Results' "rapidly" are **descriptions of a 1-hour single timepoint**, not measurements of a rate. ⚠️ **Mild abstract-over-body drift: "rapidly restored" is carried by one fixed timepoint with no earlier or later sample.**

### 2.5 🔴 Is pS14 measured at all? **No.**

**Ser14 / pS14 does not appear anywhere in the delivered body, legends or Methods.** The Methods antibody list is exhaustive and names every phospho-epitope used:

> "Additional specific antibodies used in this study were against the following proteins: 1) p53, JNK1, p-JNK1 (phosphorylation at Thr183 and Tyr185), p-ERK (Tyr204 phosphorylation) from Santa Cruz Biotechnologies, 2) p-STAT3 (Tyr705 phosphorylation) and STAT3 from New England BioLab, 3) ERK from BD Transduction Laboratory, and 4) C1q from Quidel."

**pY33 is the sole WWOX phospho-readout in this paper. Ser14 is never mentioned, never measured, never discussed.** (Caveat on the extractor: Ser14 would not conventionally be italicised, so its absence is a genuine absence, not a stripping artefact.)

### 2.6 ⚠️ "Activation" is operationally three different things, and the paper does not hold them apart

Across the paper "WOX1 activation" is used for: (i) p-WOX1 **nuclear accumulation** by IF (Fig 1); (ii) p-WOX1 **total signal** by Western (Fig 8F); (iii) **apoptotic competence** of ectopic WOX1 (Figs 2–5). These are not the same measurement and the paper slides between them. Note that (i) is a *localisation* readout reported under a *phosphorylation* label.

---

## 3 · Question 2 — 🔴 The Y33R epistasis test: real, but narrower and softer than the abstract

### 3.1 The abstract premise, verbatim-confirmed

> "A dominant negative and Y33R mutant of WOX1 blocked the apoptotic effect."

### 3.2 What the Results actually say — full quote of the load-bearing paragraph

Results section (heading delivered as "-terminal Tyr33-phosphorylated WW domain of WOX1 is responsible for C1q-induced apoptosis of DU145 cells"; the stripped italic is almost certainly *N*-):

> "We determined which domain(s) in WOX1 participates in C1q-mediated apoptosis of DU145 cells. Human and murine WWOX/FOR/WOX1 is composed of two␣-terminal WW domains, a nuclear localization sequence, and a␣-terminal short-chain alcohol dehydrogenase/reductase (SDR) domain [19–21,34; reviews]. A dominant negative-WOX1 (dn-WOX1) was designed previously, with alterations in the␣-terminal first WW domain. **dn-WOX1 is known to block the apoptotic function of p53 and prevent phosphorylation of endogenous WOX1 at Tyr33.** When DU145 cells were transiently overexpressed with dn-WOX1 (EGFP tag), the cells resisted C1q-induced apoptosis (). In controls, cells were transfected with an EGFP vector only, and the cells did not undergo apoptosis in response to C1q (data not shown or see). In positive controls, non-transfected cells were treated with staurosporine to induce apoptosis ()." *(emphasis mine)*

> "Thus, based on the above observations, the␣-terminal WW domain of WOX1 is likely to be responsible for C1q-induced activation of WOX1 for killing cancer cells. DU145 cells were transfected with the␣-terminal WW domain of WOX1 (WOX1ww with an EGFP tag) or EGFP only by electroporation and cultured for 24 hr. By time-lapse microscopy of live cells, exogenous C1q induced apoptosis of cells expressing the WW domains (). Cell shrinkage and nuclear condensation occurred approximately 100–130 min upon exposure of cells to C1q. This is a typical event of apoptosis. When DU145 cells were cotransfected with WOX1ww and dn-WOX1, **C1q-induced apoptosis was lessened** (). Tyr33 phosphorylation in WOX1 plays a key role in apoptosis both␣and␣–. **We altered Tyr33 to Arg33 in the first WW domain,, and determined that C1q did not mediate apoptosis when cells expressed this mutant protein ().** In the vector control cells, no apoptosis was observed (). C1q-mediated cell death was not observed in these control cells after a longer incubation for more than 8–24 hr…" *(emphasis mine)*

Figure 4 legend, verbatim and in full:

> "**The␣-terminal WW domain of WOX1 is associated with C1q-induced apoptosis of DU145 cells.** (A) Live DU145 cells-expressing the␣-terminal WW domain (WOX1ww; EGFP tag) were treated with C1q (1 µg/ml), followed by recording morphological changes by automatic time-lapse microscopy (one frame per 10 min). Cell shrinkage and nuclear condensation occurred approximately 100–130 min upon exposure of cells to C1q. (B) When cells were cotransfected with WOX1ww and dn-WOX1, C1q-induced apoptosis was significantly reduced. **(C) Alteration of Tyr33 to Arg33 in WOX1 did not cause C1q-mediated cell death.** (D) No apoptosis was observed in cells expressing EGFP only upon exposure to C1q. Compared to the above experiments, C1q concentration was increased for the time-lapse microscopy experiments. A representative data set is shown from 5 experiments. Approximately 100 cells were examined at the end of time-lapse microscopy. A merged photo of the cell expressing green fluorescence and the bright field image is shown (prior to challenge with C1q)."

Discussion, verbatim:

> "We determined that dominant negative and Y33R mutant of WOX1 blocked the cell death, indicating that Tyr33 activation is essential for C1q/WOX1-mediated apoptosis."

### 3.3 ✅ The test is real. 🔴 Six things constrain it, and they are all in the text above.

1. **The readout is live-cell morphology, not a death assay.** The Y33R arm (Fig 4C) is scored by **time-lapse microscopy of cell shrinkage and nuclear condensation**. The rigorous endpoints used elsewhere in the paper — SubG1 by flow cytometry (Figs 2, 3) and internucleosomal DNA fragmentation (Fig 5) — were **not applied to Y33R**. Figure 5, which is the DNA-ladder figure, lists its constructs explicitly: "WOX1, dn-WOX1 (DN), and/or p53". **Y33R is absent from Figure 5.**

2. **No statistic, and no n per condition.** Figure 4's legend gives "A representative data set is shown from 5 experiments. Approximately 100 cells were examined at the end of time-lapse microscopy." **No p-value. No mean±SD. No per-arm count.** By contrast Figs 7, 8 and 10 all carry explicit `[P]<0.001`/`[P]<0.0001` and `n`. **The load-bearing residue experiment is the least quantified experiment in the paper.**

3. 🔴 **No expression control for the mutant.** Nothing anywhere reports that EGFP-Y33R was expressed at a level comparable to EGFP-WOX1 or EGFP-WOX1ww. **A null result from a mutant construct without a matched-expression control is uninterpretable in principle** — "the mutant did not kill" and "the mutant was not there" are not distinguished by any datum in this paper. EGFP tagging makes this control trivially available (the paper elsewhere notes "The extent of green fluorescence was normally greater than 60%") and it is still not reported per-construct.

4. ⚠️ **The construct backbone is ambiguous.** The paragraph is about WOX1ww (WW domains only). The sentence says "We altered Tyr33 to Arg33 in **the first WW domain**"; the legend says "Alteration of Tyr33 to Arg33 **in WOX1**". Whether Y33R was made in **full-length WOX1** or in the **WOX1ww fragment** is not resolvable from the delivered text. Panels A and B of the same figure are WOX1ww. **I cannot determine which.** This matters: a Y33R in a WW-only fragment tests less than a Y33R in full-length protein.

5. ⚠️ **The dn-WOX1 arm is not clean, and the abstract overstates it.** The paper states that dn-WOX1 "prevent[s] phosphorylation of **endogenous** WOX1 at Tyr33" — so dn-WOX1 is not a construct-autonomous reagent; it acts in trans on the endogenous pool. And the body's verb is **"lessened"** / **"significantly reduced"**, i.e. **partial**, where the abstract says **"blocked"**. 🔴 **Abstract-versus-results drift, confirmed, on the dn arm.** (The Y33R arm's body verb — "C1q did not mediate apoptosis" — *is* consistent with "blocked".)

6. 🔴 **Y33R is never tested on the activation readout.** There is no experiment asking whether C1q still produces a p-WOX1 signal, or nuclear translocation, in Y33R-expressing cells. The residue is tested **only against the downstream apoptosis phenotype, and only in the ectopic-overexpression paradigm.**

### 3.4 What the epistasis test therefore licenses

✅ **Licensed:** *In DU145 cells overexpressing an EGFP-tagged WOX1 construct, substituting Arg for Tyr at position 33 abolishes C1q-induced apoptotic morphology* — subject to (2) no statistic and (3) no expression control.

🔴 **Not licensed:** that C1q phosphorylates WWOX at Tyr33; that Tyr33 is required for C1q to act on **endogenous** WWOX; that the C1q→WWOX activation arc runs through Tyr33 at residue level. The activation arc and the residue test are in **different experimental systems** and are never joined.

---

## 4 · Question 3 — Complement-dependent or receptor-mediated? **No receptor is named. The paper says so itself.**

### 4.1 Complement-cascade independence — asserted, and the key control is "data not shown"

Results, verbatim:

> "The enhancement of apoptosis by C1q was not due to its activation of complement cascade in the fetal bovine serum, insofar as the serum was heat-inactivated. Also, **under serum-free conditions, exogenous C1q enhanced ectopic WOX1-mediated apoptosis (data not shown).** These observations suggest that WOX1 is a downstream effector of C1q-mediated apoptosis, without involvement of complement activation." *(emphasis mine)*

🔴 **The serum-free arm is the decisive complement-independence control, and it is "data not shown."** The heat-inactivation argument is weaker than it appears: heat-inactivated *fetal bovine* serum plus purified *human* C1q is a poor substrate for a classical cascade in any case, so the manipulation does not discriminate much.

Discussion, verbatim:

> "These above-mentioned effects do not appear to be associated with activation of the complement cascade via both classical and alternative pathways. **No activated complement C3 fragments were shown to deposit on cell surface.**" *(emphasis mine)*

⚠️ **No figure, no legend and no Methods paragraph anywhere in this paper describes a C3-deposition experiment.** There is no anti-C3 antibody in the Methods antibody list. **This sentence appears only in the Discussion and is unsupported by any presented datum.** It is nonetheless *directionally concordant* with Bandini 2016's independently reported finding of unchanged C3 fragment deposition — but concordance between an unsupported Discussion sentence here and an abstract sentence there is **two unverified surfaces agreeing**, not corroboration.

### 4.2 Receptor — 🔴 none identified; one candidate explicitly flagged as untested

Discussion, verbatim:

> "We have recently shown that TGF-β1 may interact with membrane hyaluronidase 2 (Hyal-2), followed by recruiting WOX1 and the resulting WOX1/Hyal-2 complex relocation to the nuclei. **Thus, Hyal-2 could be the potential link for C1q/WOX1 signaling. Binding of Hyal-2 with C1q remains to be determined.**" *(emphasis mine)*

**The authors state in their own words that the proximal step is undetermined.** Hyal-2 is a hypothesis, not a result. No binding assay, no co-IP with C1q, no receptor blockade, no competition experiment appears anywhere in this paper.

The only other receptor language is generic literature citation, not experiment:

> "C1q interacts with specific membrane receptors to regulate immune responses,. In addition, C1q interacts with a cellular membrane type-1 matrix metalloproteinase that may regulate cancer progression and metastasis."

And the sole mechanistic gesture toward a proximal event is morphological, not molecular:

> "In agreement with our recent report, WOX1 can be associated with cell surface hyaluronidase Hyal-2."

**Verdict on Q3:** the paper claims the effect is **outside cascade activation** (on one heat-inactivation argument, one "data not shown" arm, and one unsupported Discussion sentence about C3) and **names no receptor and no proximal step**. The gap between "C1q in the medium" and "p-WOX1 in the nucleus" is entirely unfilled.

---

## 5 · Question 4 — Method class, separated

### 5.1 The separation that matters most in this paper

| Arm | System | Protein measured | Figures |
|---|---|---|---|
| **C1q → WOX1 activation** | **Endogenous**, non-transfected DU145 | **Endogenous** p-WOX1 (IF + Western) | Fig 1, Fig 8 |
| **C1q → apoptosis** | **Ectopic**, EGFP-tagged constructs by electroporation | Overexpressed EGFP-WOX1 / WOX1ww / dn-WOX1 / Y33R | Figs 2, 3, 4, 5, S1–S4 |
| **C1q ↔ WWOX colocalisation in tissue** | Human archival postmortem tissue | Endogenous C1q and p-WOX1 by IF | Fig 7 |
| **Morphology / adhesion** | Ectopic EGFP-WOX1 | Overexpressed construct | Fig 6 |

✅ **This is a genuinely useful split for LEGEND and it is the opposite of what the queue entry anticipated.** The **activation** result is on **endogenous protein**. The **functional (apoptosis)** result is **entirely ectopic**.

### 5.2 🔴 The Aldaz critique applies squarely to the apoptosis arm, and the paper offers it no defence

Per `PAPER 053` and the Chang↔Aldaz adjudication, the dispute turns on **necessity vs sufficiency**: knockdown of endogenous WOX1 tests necessity and cannot be a delivery artefact; overexpression-induced apoptosis can.

**There is no knockdown, no siRNA, no shRNA and no knockout of WWOX anywhere in this paper.** The strings do not occur in the delivered body or Methods. The only knockout mentioned is a *cited* murine phenotype, not an experiment performed here:

> "Murine WOX1/Wwox is critical for postnatal survival, insofar as the knockout mice could survive for only one month,."

**The apoptosis arm is 100% on the sufficiency side.** Moreover the paper's own vector control demonstrates that endogenous WOX1 is insufficient:

> "In controls, C1q did not induce apoptosis in DU145 cells overexpressing EGFP vector only ()."

> "…BCC cells expressing EGFP were resistant to C1q-mediated cell death, whereas hWOX1-expressing cells were sensitive to C1q ()."

🔴 **So in cells with only endogenous WWOX, C1q produced no apoptosis.** The killing phenotype required supraphysiological WOX1 delivered by electroporation — precisely the configuration Aldaz attributes to vector/overexpression artefact. **The Y33R and dn-WOX1 experiments, being run inside that same overexpression paradigm, inherit the critique in full**; a residue requirement *within* an artefactual phenotype does not rescue the phenotype.

⚠️ **Partial mitigation, stated fairly:** the **activation** arm (Fig 1 add-back on endogenous p-WOX1; Fig 8F ~50% loss of endogenous basal p-WOX1 under ΔC1q, [P]<0.001, n=3) is *not* an overexpression experiment, and the Aldaz overexpression critique does not reach it. It remains subject to the separate antibody-specificity concern of § 2.3.

### 5.3 Cell lines, primary cells, in vivo

- **Cell lines only, all transformed:** DU145 (prostate carcinoma, principal), MCF7 (breast, Fig S2), SH-SY5Y (neuroblastoma, Fig S3), SK-N-SH (neuroblastoma, "data not shown"), BCC skin basal cell carcinoma stable transfectants.
- **No primary cells. No primary neurons. No iPSC. No organoid.**
- 🔴 **No in vivo experiment of any kind.** No animal was used. There is no mouse, no xenograft, no injection.
- **Human material:** archival postmortem prostate only, immunofluorescence only, **n = 5 per group**:
  > "The tissues included patients with benign prostatic hypertrophy (BPH), prostatic adenocarcinoma, and age-matched normal prostate tissues (5 each)."
  > "C1q is significantly downregulated in BPH and prostate cancer, as compared to age-matched prostate tissues ([P]<0.0001, n = 5; Student's [t] test)."
  This is a **cross-sectional expression correlation**, not a mechanism, and it says nothing about direction of causation.

### 5.4 ⚠️ Prostate cancer cells are not neurons — and the neural data here are weaker still

The principal system is **DU145 human prostate carcinoma**, a transformed epithelial line. It is not a neuron, not post-mitotic, not synaptically connected, and shares neither the proteostatic environment nor the excitability of the cell type that matters for a WWOX-DEE genotype.

The paper's only neural-lineage data are **SH-SY5Y and SK-N-SH neuroblastoma lines**, both at **supplementary** level (Figs S3, S4), both **ectopic EGFP-WOX1 overexpression**, one of them "data not shown". **Neuroblastoma lines are transformed proliferating cells, not neurons.** Nothing in this paper is a neuron.

🔴 **And the direction the authors themselves project into neurons is toward death, not rescue:**

> "Indeed, C1q has been implicated in the pathogenesis of neuronal death in the neurodegenerative diseases such as in Alzheimer's disease,. **There is a strong possibility that C1q activates WOX1 in neurons, which ultimately leads to cell death.** Conceivably, the concentrations of C1q in the brain matrix and the cytosolic levels of neuronal WOX1 will determine the extent of C1q/WOX1 signaling and cell death." *(emphasis mine)*

This is speculation, not data — but it is the authors' own reading of what their axis would do in a neuron, and it is a **pro-death** reading.

---

## 6 · Question 5 — Direction, and whether activation can be raised when protein is scarce

### 6.1 Direction, plainly

✅ **C1q → WWOX activation state: UP.** This is consistently supported across two independent endogenous-protein readouts in the same cell line:

- **Removal lowers it:** "Under C1q-free conditions (ΔC1q serum), the basal activation of WOX1 was significantly reduced (∼50% reduction; [P]<0.001 …; n = 3)."
- **Add-back restores it:** "Reconstitution of ΔC1q serum with purified C1q rapidly induced p-WOX1 accumulation in the nuclei ()."

✅ **A genuinely relevant secondary finding: the effect is on phospho-state, not on WWOX abundance.** Verbatim:

> "Expression of ERK, WOX1, MEK1, and p53 was not significantly affected by the above-mentioned culture conditions (; data not shown for MEK1)."

> "In the absence of C1q or C6, expression of WOX2 is downregulated, whereas **WOX1 expression is not affected**." *(emphasis mine)*

**Total WOX1 protein is unchanged while pY33 falls by ~50%.** That is the cleanest statement in this paper that activation and abundance are separable axes — which is the reason LEGEND opened this file. ⚠️ Note the paper simultaneously reports that C1q/C6 depletion *does* reduce the **WOX2** isoform and p-ERK, so the C1q manipulation is not WWOX-phospho-selective.

### 6.2 🔴 Does the paper bear on raising activation when protein is scarce? **Yes — and it points the wrong way.**

As predicted in the task, the paper never tests a low-WWOX condition. But it is not silent: **three separate statements each indicate the mechanism requires WWOX protein to be present, and scales with how much there is.**

1. **The functional effect needed overexpression.** C1q did nothing to vector-only cells (§ 5.2). Endogenous WWOX levels in DU145 were not sufficient for the phenotype.
2. **The effect was dose-related in the direction of more protein.** Figure S1 legend, verbatim: "DU145 cells were transfected with various amounts of EGFP-WOX1 (tagged with EGFP; 2.5–10 µg) by electroporation… C1q enhanced WOX1-induced apoptosis of DU145 cells (see the increases in SubG1 phase but decreases in the G0/G1 phase)." **More WWOX, more effect.**
3. 🔴 **The authors state the limitation explicitly.** Discussion, verbatim:
   > "Nonetheless, the **C1q/WOX1 signaling could be less efficient in cancers, as many advanced cancer cells are deficient in the wild type WWOX/WOX1**,." *(emphasis mine)*

   And in the same neuronal passage: "the concentrations of C1q in the brain matrix and **the cytosolic levels of neuronal WOX1** will determine the extent of C1q/WOX1 signaling".

**The paper's own position is that WWOX deficiency makes this axis less effective, not more.** ⚠️ Caveat stated fairly: the paper never *measures* WWOX protein level in any cell it uses, and never titrates downward, so this is the authors' inference plus the vector-control null — not a scarce-protein experiment. But it is the opposite of the finding LEGEND would need.

---

## 7 · Abstract-versus-Results check (mandated)

| # | Abstract says | Body says | Assessment |
|---|---|---|---|
| 1 | "A dominant negative and Y33R mutant of WOX1 **blocked** the apoptotic effect." | dn arm: "C1q-induced apoptosis was **lessened**" / "significantly reduced". Y33R arm: "C1q did not mediate apoptosis". | 🔴 **Drift on the dn arm** — partial reported as blocked. Y33R arm consistent. |
| 2 | "exogenous C1q **significantly** induced apoptosis of WOX1-overexpressing DU145 cells" | Fig 2 legend reports "A representative data set from 3 experiments is shown in the bar graph" — **no p-value, no test**. | ⚠️ "Significantly" is not backed by a reported statistic in the corresponding legend. |
| 3 | "Exogenous C1q **rapidly** restored the WOX1 activation … in **less than 2 hr**." | Single fixed 1-hr IF timepoint; no kinetic series. | ⚠️ Rate language from one timepoint. Verbatim-true, evidentially thin. |
| 4 | Title: "Complement C1q Activates Tumor Suppressor WWOX to Induce Apoptosis in Prostate Cancer Cells" | Apoptosis required **ectopic** WOX1; vector-only cells did not die. | 🔴 Title generalises a phenotype that the paper's own control shows does not occur at endogenous levels. |
| 5 | "C1q did not enhance p53-mediated apoptosis." | Body reports something stronger and directionally awkward: "**Intriguingly, C1q suppressed the DNA fragmentation in the p53/WOX1-expressing cells.**" | ⚠️ **A suppressive effect of C1q on death is reported in the body and softened to a null in the abstract.** The less convenient result is the one that got compressed. |

**No outright inversion found.** Four over-statements and one softened inconvenient result. The task's three abstract-derived premises are each **verbatim-accurate as abstract text**; two of the three (the add-back, the residue) survive contact with the body, with the constraints set out above; the third (dn "blocked") does not survive as stated.

---

## 8 · VERDICT

### Proposition under test: *"C1q raises WWOX activation state through Tyr33, demonstrated at residue level."*

# 🟡 PARTIALLY SUPPORTED

**The narrow version that this paper supports:**

> In human DU145 prostate carcinoma cells, **removing C1q from serum lowers the basal Tyr33-phosphorylated WWOX signal by ~50% ([P]<0.001, n=3, Western blot) and shifts it to the cytoplasm, without changing total WWOX protein; adding purified C1q back restores nuclear p-WOX1 within 1 hour** — both measured on **endogenous** protein with an **in-house, non-validated rabbit anti-pTyr33 antibody**. **Separately**, in the same cells **overexpressing** an EGFP-tagged WWOX construct, a **Y33R substitution abolishes C1q-induced apoptotic morphology** by time-lapse microscopy — **with no statistic, no n per arm, no construct-expression control, and ambiguity as to whether the mutation was made in full-length WWOX or in the WW-domain fragment.**

**Why not `SUPPORTED`.** Three independent gaps, any one of which would be disqualifying for a residue-level claim:

1. 🔴 **The residue test and the activation measurement are never joined.** Y33R is tested only against downstream apoptosis in an overexpression system. **No experiment asks whether C1q still produces a p-WOX1 signal in a Y33R background.** "C1q raises activation *through* Tyr33" therefore rests on an inference across two non-overlapping experimental systems.
2. 🔴 **The antibody is not validated against the mutant.** The one control that would make "pY33" a residue-level readout — staining or blotting Y33R with the anti-pTyr33 antibody — was available (the mutant exists) and is not reported.
3. 🔴 **The residue experiment is the least quantified in the paper**, and lacks the expression control without which a mutant null result cannot be distinguished from absent protein.

**Why not `CORRELATIVE ONLY`.** Because a real **add-back** exists (depletion → reconstitution → restoration, on endogenous protein), and a real **point-mutant epistasis arm** exists. Both are genuine interventional designs. The task was right that this paper contains the three things Bandini 2016 lacks. They are simply softer, and less connected to each other, than the abstract implies.

---

## 9 · What this would and would not give a loss-of-function genotype

**It would give** a demonstration that WWOX **activation state (pTyr33) and WWOX abundance are separable and separately regulated** — total WWOX protein was unchanged while pTyr33 fell by half — which is a real answer to the axis LEGEND opened this file for: an activation-state readout is not defeated *in principle* by the abundance question, and an extracellular input can move it within an hour.

**It would not give** anything usable when protein is scarce. The paper's functional effect required electroporated overexpression and was **absent in vector-only cells at endogenous WWOX levels**, it was **dose-related to how much WWOX was supplied**, and the authors state plainly that "C1q/WOX1 signaling could be less efficient in cancers, as many advanced cancer cells are deficient in the wild type WWOX/WOX1." Nothing here suggests activation can be raised when there is little protein to activate; the evidence runs the other way.

**Nor would it transfer.** Every datum is from transformed proliferating lines — prostate carcinoma principally, with neuroblastoma lines only in supplementary overexpression panels; **there is no neuron and no in vivo experiment in this paper**, no proximal receptor is identified (the authors flag Hyal-2 as untested), and the apoptosis arm sits entirely on the sufficiency side of the Chang↔Aldaz necessity-vs-sufficiency line with no knockdown anywhere.

🔴 **Finally, the direction of the phenotype is death.** The output measured throughout is apoptosis, and the authors' own extrapolation is that "C1q activates WOX1 in neurons, which ultimately leads to cell death." For a genotype whose problem is neuronal dysfunction and loss, an axis whose demonstrated endpoint is apoptosis is **not directionally safe on its face**, whichever way it is pushed. This file establishes biology only; **no intervention is proposed and none is warranted from this surface.**

---

## 10 · Repository findings recorded (read-only — nothing edited)

1. 🔴 `FT-108` wikilinks this paper to `[[paper_registry_current#CORPUS P331]]`. The correct entry is **`CORPUS P330`** (`LIT link: LIT-0330`). `P331` is Zhu et al. 2021, *Vet Microbiol*, PMID 33191002 (Marek's disease virus miR-155). `c1q_wwox_activation_audit_20260921.md` § 3 inherited the same wrong ID.
2. ⚠️ `FT-108` and the task brief cite the paper as "Hsu L-J, … Chang N-S 2009". First author is **Hong Q**; Hsu L-J is the tenth of eleven authors. The registry entry `CORPUS P330` is correct ("Hong et al.").
3. ✅ `FT-108`'s substantive claims are confirmed: open access (CC BY 4.0), never deep-dived, `Claim links: none — triage only`. The paper is now read in full; the queue entry's "Next action: acquisire da PMC (`PMC2685983`) e leggere integralmente" is discharged by this file.
4. ⚠️ The PubMed MCP extractor **silently deletes italicised tokens** — here the italic gene symbol *WWOX*, *N*-/*C*- terminal prefixes, *in vitro*/*in vivo*, italic *P* and *t*, and all inline figure cross-references. Roman-type protein symbols survive. This is a third distinct extractor failure mode, milder than the total stripping seen on PMID 41153369 and 41390778, and it is **silent**.

**No commit candidate produced. No canonical file read for modification or modified.**
