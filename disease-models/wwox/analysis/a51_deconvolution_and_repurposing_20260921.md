# A51 deconvolved — what the compound actually is, and whether anything can substitute for it

**Date:** 2026-09-21 · **Actor:** Scientist B · **Node:** `TX004_A51_DECONVOLUTION_AND_REPURPOSING`

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, the registries and every
> ledger. Nothing promoted, nothing committed.
>
> 🔴 **BLOCK-1 observed. No safety triage was run and no druggability score is assigned anywhere in this file.**
> What follows is a census of what is *published*, with the point where the evidence stops named explicitly each
> time. No compound here is proposed for use in any person.
>
> **Nothing here is medical advice.** No dose, route, schedule or indication is formulated for any patient.

---

## 0. Read depth declared up front

| PMID | Identity | Depth **this session** | Returned body length | Figure access |
|---|---|---|---|---|
| **42397075** | Steinberg … Aqeilan 2026, *Brain* — the organoid A51 experiment | 🔴 **not fetchable — no PMCID exists** (converter returns pmid + doi only). Worked from receipt `FTR-20260810-42397075-04` and its **30-locator** manifest | **0 bytes** | none. All panel values are **prior-session figure attestations**, attributed as such |
| **40665325** | Ball *et al.* 2025, *J Hematol Oncol* — **BTX A51 Phase I first-in-human** | **abstract read in-act, in full** | abstract only | none |
| **39483885** | the same study as a *Research Square* preprint | abstract read in-act | abstract only | none |
| **42714273** | Flor *et al.* 2026, *J Virol* — BTX-A51 as a CK1 pharmacological tool | abstract read in-act | abstract only | none |
| **39140066** · **41704356** · **42669983** | medicinal-chemistry papers using BTX-A51 as the reference CK1α/CDK7 chemotype | abstracts read in-act | abstract only | none |
| **34696771** · **34359754** · **32562591** · **38183981** | MYC-directed agents in CNS-tumour contexts | abstracts read in-act | abstract only | none |
| — | PubMed `BTX-A51` | executed | 🔴 **`total_count: 6` — the entire published record of this compound** | n/a |
| — | 5 further PubMed queries (MYC×CNS; tankyrase×CNS; brain-penetrant tankyrase; MYC brain-penetrant PK; CK1α/Ben-Neriah) | executed | see §3 | n/a |

🔴 **Declared limitation, and it bounds §1.** The organoid paper cites a prior characterisation for A51 as its
**reference 62**. That paper has **no PMC deposit and no retrievable reference list from this environment**, so
**the citation hop could not be followed to its terminus.** The identification in §1 is therefore built from
convergent external evidence, and is labelled `INFERENZA` — strong, but not closed.

⚠️ **DOI verification, stated honestly.** A `convert_article_ids` pass over all seven cited PMIDs returned
`API_ERROR`; a smaller batch succeeded. DOIs below are taken from the authoritative `identifiers.doi` field of
the in-act `get_article_metadata` responses, **not reconstructed**. One discrepancy is recorded in §7.

---

## 1. The direct answer

**A51 is almost certainly BTX-A51, and it is not a MYC inhibitor at all.** BTX-A51 is *"a first-in-class oral
small molecule inhibitor of casein kinase 1α (CK1α) and cyclin-dependent kinase (CDK) 7 and 9"*, developed from
the laboratory of Yinon Ben-Neriah at the Hebrew University–Hadassah Medical School — **the same institution as
the Aqeilan laboratory**, and the organoid paper states its A51 was *provided by the Ben-Neriah group*. That
makes three independent points of coincidence: institution, the *"multi-kinase"* descriptor, and the joint
Wnt-plus-MYC activity profile. **If the identification holds, the deconvolution is already done by pharmacology
and needs no new experiment: the "MYC" arm is almost certainly CDK9-mediated suppression of RNA-polymerase-II
elongation — a global short-half-life-transcript effect for which MYC is the canonical readout, not a selective
target** (the Phase I reports *"reduced the expression of MCL1 and RNA polymerase II phosphorylation"*).
🔴 **And the Wnt arm may point the wrong way.** CK1α is the priming kinase of the β-catenin destruction complex,
and an independent 2026 study using BTX-A51 as a CK1 tool reports *"a significant increase in β-catenin protein
levels"* — the **opposite** direction from the one `TX-004` requires. ⇒ **`TX-004`'s mechanism sentence is
doubly wrong: the compound is not MYC-selective, and its Wnt effect is contested in direction.**
On procurement, the answer is a clean negative in both arms. BTX-A51 is **a real clinical-stage drug, not a tool
compound** — oral, Phase I complete in adults with relapsed/refractory AML and MDS (`NCT04872166`), RP2D
**21 mg three days/week** — but the **entire published record of the compound is six papers**, and **not one of
them mentions brain, CNS or the blood–brain barrier**; its declared toxicities are gastrointestinal at high
frequency with **hepatic dose-limiting toxicity**; and the cohort's median age was **75**, with **no paediatric
exposure of any kind.** For the substitution: **no selective MYC-directed agent with published CNS exposure data
exists** — every CNS-context use found is in vitro in tumour cells — and on the Wnt side `TX-004` already records
intestinal and bone toxicity with high paediatric caution, to which this node adds that **BBB penetration remains
unestablished for the tool compounds.** ⇒ **A51 is a clinical-stage but CNS-uncharacterised oncology drug whose
named mechanism is wrong in the organoid paper, and there is no procurable selective substitute for either arm.
`TX-004`'s near-term path is closed, and the next session should not hope otherwise.**

---

## 2. Task 1 — what A51 is

### 2.1 What the organoid paper says, verbatim (prior-session locator, receipt-backed)

> "we performed a MYC inhibition experiment, using a multi-kinase inhibitor (A51) established to suppress Wnt and MYC expression"

`surface: body` · Results p. 11 · `PMID 42397075`, LEGEND manifest entry 17. Dose **125 nM**, weeks **8 → 15**,
compound **provided by the Ben-Neriah group** (supplementary File009, *"MYC inhibition"*). The section is titled
*"MYC dysregulation mediates neurogenic defects"*. 🔴 **The paper names its own reagent as non-selective in the
sentence that introduces it. It hides nothing; the over-reading is downstream.**

### 2.2 The identification, and its evidence

| Convergence point | Evidence |
|---|---|
| **Name** | The compound is called **A51**; the only compound named A51 in the pharmacological literature is **BTX-A51** / **BTX A51** |
| **Provenance** | The organoid paper states the compound was **provided by the Ben-Neriah group**. **Yinon Ben-Neriah, The Lautenberg Center, Hebrew University–Hadassah Medical School**, is an author of the BTX A51 Phase I — the same institution as the Aqeilan laboratory |
| **Descriptor** | *"multi-kinase inhibitor"* matches *"inhibitor of casein kinase 1α (CK1α) and cyclin-dependent kinase (CDK) 7 and 9"* — three kinases |
| **Activity profile** | Wnt **and** MYC in one agent is exactly what a CK1α + CDK9 dual activity produces: CK1α sits in the β-catenin destruction complex, CDK9 controls MYC-dependent transcriptional elongation |

**Status: `INFERENZA`, strong but not closed.** 🔴 **What would close it in one step:** read **reference 62** of
`PMID 42397075`, or the *"MYC inhibition"* subsection of supplementary **File009**, either of which names the
compound's source publication. Both are in the artefact bundle that a prior session held and this environment
cannot reach.

### 2.3 What BTX-A51 actually does — verbatim, in-act

> "BTX A51, a first-in-class oral small molecule inhibitor of casein kinase 1α (CK1α) and cyclin dependent kinase (CDK) 7 and 9, induces apoptosis of leukemic cells by activating p53 and inhibiting expression of Mcl1."

`surface: abstract` · `PMID 40665325`.

> "BTX A51 increased the expression of p53 and reduced the expression of MCL1 and RNA polymerase II phosphorylation in pre- and post-treatment immunocytochemistry studies."

`surface: abstract` · same. **This is the pharmacodynamic readout of CDK9 inhibition: loss of RNA Pol II CTD
phosphorylation and collapse of short-half-life transcripts.** MCL1 is the canonical one in leukaemia; **MYC is
the canonical one everywhere else.**

> "Starting from BTX-A51, a CK1α inhibitor that also targets CDK7 and CDK9, we designed and synthesized a series of 2,4-diaminopyrimidine derivatives as potent CDK7 inhibitors."

`surface: abstract` · `PMID 39140066` — an independent medicinal-chemistry group treating BTX-A51 as the
reference chemotype for this triple activity.

> "compound … exhibited potent inhibitory activity against CK1α with an IC of 10.96 nM, representing a 9-fold increase in potency as compared to BTX-A51, **the only CK1α inhibitor currently in clinical development**."

`surface: abstract` · `PMID 41704356`. ⚠️ the subscript of `IC50` is deleted by the extractor — the value is
quoted as returned and the deletion is stated rather than silently repaired.

### 2.4 🔴 The finding that changes `TX-004`: the Wnt direction is contested

> "Additionally, BTX-A51 treatment influenced the β-catenin pathway, resulting in a significant increase in β-catenin protein levels and β-catenin colocalization with p65."

`surface: abstract` · `PMID 42714273`, *J Virol* 2026, using BTX-A51 *"as a pharmacological tool to investigate
the role of CK1"*.

**Why this matters, stated carefully.** CK1α phosphorylates β-catenin at Ser45, the priming event for the
destruction complex. **Inhibiting CK1α is expected to stabilise β-catenin, i.e. to raise Wnt output, not lower
it.** The independent study reports exactly that. The organoid paper describes its compound as *"established to
suppress Wnt"*. **The two statements are in tension, and `TX-004`'s entire directional premise — WWOX loss
de-represses Wnt, therefore the lever is Wnt INHIBITION — depends on which is right.**

⚠️ **Boundaries on this, and they are real.** The β-catenin observation is (i) in **virus-infected cells**, not
neural tissue; (ii) **one paper**; (iii) read at **abstract level only**; and (iv) "β-catenin protein level" is
not the same measurement as "Wnt transcriptional output", which is what the organoid paper's descriptor may
refer to. ⇒ **`FLAG`, not a refutation.** But the consequence for the node is immediate and does not depend on
resolving it: **if the Wnt arm is null or inverted, the rescue A51 produced was carried by the CDK9/MYC arm**,
which is the arm `TX-004` names — and `TX-004` would be right for the wrong reason, on a compound that is not
MYC-selective.

---

## 3. Tasks 2 and 3 — the agent table

**Legend.** `Procurable?` means: does a supply route exist for a laboratory experiment — **not** a clinical
judgement of any kind. Nothing in this table is a safety assessment.

| Agent | Mechanism | Selectivity | CNS exposure evidence | Paediatric data | Procurable? | What would make it testable in a WWOX organoid |
|---|---|---|---|---|---|---|
| **A51 / BTX-A51** | CK1α + CDK7 + CDK9 inhibitor; ↑p53, ↓MCL1, ↓RNA Pol II phosphorylation | 🔴 **none — three kinases, two pathways.** The paper's own descriptor | 🔴 **ZERO.** `brain`, `CNS`, `blood–brain barrier` appear in **none of the 6 published records**, all read at abstract level in-act. An informative zero over a complete record set | 🔴 **none.** Phase I median age **75**, range 22–84 | 🟡 **Yes, by collaboration** — it is already in the Aqeilan laboratory's reach via the Ben-Neriah group, and that is how the organoid experiment happened | Already done once. What is missing is **dose–response, a treated WT arm, independent differentiations and blinding** — see §5 |
| **MYCi975 (Myci975)** | small-molecule MYC inhibitor (MYC–MAX disruption class) | 🟡 nominally MYC-directed | 🟡 **CNS-context but not CNS-exposure.** *"a novel small-molecule Myc inhibitor, Myci975, alleviated TMEM44-AS1-promoted the growth of glioma cells"* — **glioma cells in culture.** 🔴 No brain PK, no BBB ratio, no intracranial model in that abstract | 🔴 none found | 🟢 Yes — a research chemical | Would need **its own CNS-irrelevant status accepted**: an organoid assay does not require BBB crossing, so MYCi975 is testable *in the dish* today. **BBB only matters for the step after** |
| **Omomyc / OMO-103** | dominant-negative MYC-dimerisation mini-protein | 🟢 the most MYC-selective agent class that exists | 🟡 used in **Group 3 medulloblastoma** work to define MYC-dependent transcripts — a **genetic/protein tool in cells**, not a CNS-delivered drug in the record found | 🔴 none found | 🟡 as a construct, yes; as a deliverable protein, not from here | Testable in organoids **as a construct**, which converts it from a pharmacology question into a genetics one — and that is arguably the cleaner experiment |
| **10058-F4** | MYC–MAX disruptor, classic tool | 🟡 partial | 🟡 used in **glioblastoma cells** in vitro | 🔴 none | 🟢 Yes | Same as MYCi975: dish-testable now |
| **γPNA c-Myc inhibitor** | genomic-DNA-targeted transcription block | 🟢 sequence-specific | 🔴 none — *"cell-line- and patient-derived xenografts"*, no CNS | 🔴 none | 🔴 bespoke | Not a near-term option |
| **XAV939 / tankyrase inhibitors** | tankyrase inhibition → axin stabilisation → ↓Wnt | 🟢 on-target for Wnt | 🔴 **not established.** LEGEND's `R-03` already records BBB *"not established for the tool compounds"*; this node's targeted searches for a brain-penetrant tankyrase inhibitor returned **`total_count: 0`** | 🔴 none; `TX-004`/`R-03` already record **intestinal-crypt turnover and bone toxicity**, high paediatric caution | 🟢 Yes — a research chemical | Dish-testable now, and it is **already the named comparator** in LEGEND's `E-10` (XAV939 vs CHIR99021 on organoid cortical layering) |
| **LGK974/WNT974 · ETC-159 · PRI-724 · G007-LK** | upstream Wnt (PORCN) or β-catenin–CBP | 🟢 on-target | 🔴 no CNS-exposure evidence surfaced by the targeted query | 🔴 none | 🟡 variable | Not needed — XAV939 already occupies the comparator slot |

### 3.1 The measured absences, stated as measurements

- `BTX-A51` → **`total_count: 6`**. All six abstracts read in-act. **`brain` / `CNS` / `blood–brain barrier`
  appear in none of them.** These are roman-type tokens; the extractor could not have deleted them.
- `brain-penetrant tankyrase inhibitor pharmacokinetics brain exposure mouse` → **`total_count: 0`.**
- `MYCi975 OR "MYC inhibitor" brain penetrant pharmacokinetics in vivo tumor MYC degradation` → **`total_count: 0`.**
  ⚠️ Both zeros are from **over-conjoined queries** and are therefore weak evidence of absence; they are reported
  as query results, not as biological zeros. The **strong** zero is the BTX-A51 one, because it is exhaustive
  over a six-record corpus.
- `(MYCi975 OR MYCi361 OR Omomyc OR OMO-103 OR "MYC inhibitor") AND (brain OR BBB OR CNS OR glioma OR neural)` →
  **`total_count: 17`**, of which the CNS-context ones inspected are **all in vitro in tumour cells**.

### 3.2 🔴 The observation that reorganises task 3

**BBB penetration is not the gate for the next experiment.** The experiment that matters is in **organoids**, and
an organoid has no blood–brain barrier. ⇒ **MYCi975, 10058-F4 and XAV939 are all testable in a WWOX organoid
today**, and their lack of CNS data bears only on what would happen *after* a positive result. Conversely,
**BTX-A51's clinical maturity buys nothing** for that experiment — its value there is as the comparator that
reproduces the published effect.

**That inverts the framing the node inherited.** The blocker is not procurement of a CNS-suitable agent; it is
that **nobody has run the selective arms in the dish**, and every agent needed to do so is an ordinary research
chemical.

---

## 4. Task 4 — the two-sided risk, stated rather than only the upside

🔴 **`CLAIM 028` and `TX-004`'s own caution bind here and are not restated as decoration.** `TX-004` records
explicitly that *"lower MYC/Wnt = better" is NOT a safe default*, and `CLAIM 028` that *"more WWOX = better"* is
not either. The context-dependence is the same object.

**What `PMID 42397075` actually found makes the risk concrete.** **MYC is the top-upregulated gene in radial
glia** — a **progenitor proliferation compartment in a developing brain**. An agent that suppresses MYC there is
not correcting a lesion in a post-mitotic tissue; **it is damping a proliferation program during
corticogenesis.** And the A51 result shows precisely that ambivalence: SOX2⁺ fell from ≈60 % to ≈33 % — which is
scored as normalisation **because the knockout was above wild type** — while **SATB2⁺ and CTIP2⁺, the neurons the
progenitors are supposed to produce, did not move at all** (`ns` KO-vs-A51 on both; CTIP2⁺ remained `****` below
WT). `figure-attestation-from-prior-session`, Suppl. Fig. 7F–G, read at 170 ppi and re-read at 258 ppi.

⇒ **The honest reading is that A51 reduced the progenitor excess without increasing the neuronal output** — and
a reduction in progenitors that does not become neurons is **exactly what "preventing normal corticogenesis"
would also look like.** `DL-THER-089` already writes this as an open BLOCK-1 question: *the window between
reducing excess progenitors and preventing normal development is measured nowhere in this work*, which tests
**one dose on one genotype with no treated wild-type arm.** **This node does not close it and adds a second
reason it must not be closed by assumption: the compound also raises p53** — a pro-apoptotic response in a
compartment that the same literature shows already carries DNA damage and a compromised apoptotic checkpoint in
WWOX deficiency.

---

## 5. Task 5 — the experiment, updated by tasks 1–3

**The Wave-1 four-arm design survives, and two things about it change.**

**Change 1 — the arms are now named by mechanism, not by pathway label.** Because A51 is CK1α + CDK7/9, the two
arms to separate are **CDK9/transcriptional-elongation** and **CK1α/β-catenin**, not "MYC" and "Wnt".

**Change 2 — one arm is procurable and one is not, and this is the answer to "which".**
- 🟢 **The Wnt arm is procurable today**: XAV939 is an ordinary research chemical, is already LEGEND's named
  comparator in `E-10`, and needs no CNS property to be tested in an organoid.
- 🟡 **The MYC arm is procurable only as a proxy**: MYCi975 and 10058-F4 are available and dish-testable, but
  neither is a clean CDK9 substitution. **The mechanistically exact arm is a selective CDK9 inhibitor**, which
  this node did not census and which is the one gap a follow-up should close first.
- 🔴 **A51 itself is procurable only by collaboration** with the group that supplied it.

**The design, restated:**

> **In WWOX-KO and WOREE patient-derived cortical organoids: vehicle · A51 · a selective CDK9 inhibitor · XAV939,
> each at three doses, with a treated wild-type arm at every dose, across ≥3 independent differentiations and
> ≥2 clones per line, blinded and randomised, reading both the progenitor endpoints A51 moved (SOX2⁺,
> SOX2⁺MYC⁺, NEUN⁺) and the layer endpoints it did not (SATB2⁺, CTIP2⁺), plus nuclear β-catenin as a direct test
> of which direction the CK1α arm actually drives.**

The added β-catenin readout is new and cheap, and it settles §2.4 inside the same experiment.

**What each outcome decides.** CDK9 arm reproduces A51 ⇒ the effect is transcriptional-elongation suppression and
`TX-004`'s MYC label is a proxy, not a target. XAV939 reproduces it ⇒ the lever is `R-03`, which inherits
`R-03`'s paediatric liabilities. Neither reproduces it ⇒ **A51's effect is off-target and the only pharmacological
rescue in human WWOX-deficient neural tissue dissolves** — the cheapest possible way to learn that.

---

## 6. What LEGEND already knew · what is new

### 6.1 Already held — used, not re-derived

- `DL-THER-089`: A51 is a multi-kinase inhibitor, not a MYC inhibitor; **125 nM, weeks 8→15**, Ben-Neriah group;
  the full Suppl. Fig. 7F–G split (SOX2⁺ ≈60→33 `ns` vs WT; SOX2⁺MYC⁺ ≈72→50 `ns` vs WT; NEUN⁺ ≈6→18 `*`;
  **SATB2⁺ and CTIP2⁺ `ns`**); the open BLOCK-1 Wnt-during-corticogenesis question; `IPOTESI`, not a candidate.
- `TX-004` / `R-03`: Wnt direction resolved as **hyper**activation; tankyrase inhibitors carry **intestinal and
  bone toxicity**, BBB **not established**, **no paediatric-profiled candidate**; *"lower MYC/Wnt = better" is
  NOT a safe default*.
- `E-10`: XAV939 **vs** CHIR99021 on organoid cortical layering, with nuclear β-catenin measured **first**.
- `CLAIM 028`; the three declared method limits of the A51 experiment (no independent differentiations, no
  randomisation or blinding, one clone).
- `NS-015`: an open scouting item for **Wnt/tankyrase inhibitors with a paediatric profile** — still open.

### 6.2 New in this node

1. 🔴 **A51 is identified: BTX-A51, a CK1α + CDK7 + CDK9 inhibitor** — `INFERENZA` on four convergent points
   (name, Ben-Neriah provenance, "multi-kinase", dual Wnt/MYC profile). **LEGEND held only the string "A51".**
2. 🔴 **It is a clinical-stage drug, not a tool compound**: oral, Phase I complete in adults (`NCT04872166`),
   31 patients, doses 1–42 mg, **RP2D 21 mg three days/week**, *"the only CK1α inhibitor currently in clinical
   development"*.
3. 🔴 **Its "MYC inhibition" is almost certainly CDK9-mediated transcriptional-elongation suppression** —
   *"reduced … RNA polymerase II phosphorylation"* — i.e. **a global short-half-life-transcript effect, not a MYC
   target.** `TX-004`'s mechanism sentence names a target the reagent does not have.
4. 🔴 **The Wnt direction is contested and may be inverted**: CK1α is the β-catenin priming kinase, and an
   independent study reports BTX-A51 producing *"a significant increase in β-catenin protein levels"*. **If so,
   the organoid rescue was carried by the CDK9 arm and the compound pushed Wnt the way `TX-004` says is harmful.**
5. 🔴 **Zero CNS data, measured exhaustively**: the compound's entire published record is **six papers**, all read
   in-act at abstract level, and **none mentions brain, CNS or the blood–brain barrier.**
6. 🔴 **Toxicity and age profile, published**: nausea 67 %, emesis 63 %, hypokalemia 53 %, diarrhoea 40 %; **two
   hepatic dose-limiting toxicities**; no treatment-related deaths; **median age 75; no paediatric exposure.**
   Efficacy modest — 3/31 (10 %) CRi. **Recorded as published fact; no triage, no score.**
7. ✅ **No selective MYC-directed agent with published CNS exposure exists** — every CNS-context use found is
   in vitro in tumour cells (MYCi975 in glioma cells; 10058-F4 in glioblastoma cells; Omomyc as a cellular tool
   in Group 3 medulloblastoma).
8. 🔴 **The framing inversion:** **BBB penetration is not the gate**, because the decisive experiment is in
   organoids. **The selective arms are ordinary research chemicals and nobody has run them.** The blocker is
   effort, not procurement.
9. ✅ **A new, cheap readout for the deconvolution experiment**: measure **nuclear β-catenin** in the same
   organoids and settle the CK1α direction inside the existing design.

---

## 7. Corrections, with exact file and line coordinates

**W6-C1 — `TX-004`'s mechanism sentence names a target its only reagent does not have.**
- **File:** `disease-models/wwox/therapeutics/therapeutic_strategies_current.md` · the **TX-004** block
  (`### TX-004 — Wnt / MYC modulation (downstream)`), `**Mechanism:**` line
- **Exact current text:** `- **Mechanism:** Steinberg 2024 identifies **MYC overexpression** as a key node of hyperexcitability in WWOX organoids, corrected by rescue. Wnt-adjacent. Wnt/tankyrase inhibitors would act *downstream*, without repairing WWOX → potentially genotype-agnostic.`
- **Exact proposed replacement:** `- **Mechanism:** `PMID 42397075` identifies **MYC as the top-upregulated gene in WWOX-deficient radial glia** — a **neurogenesis** compartment, not a hyperexcitability one. 🔴 **Two corrections (2026-09-21).** (i) *"corrected by rescue"* conflates two interventions: **WWOX restitution** (AAV9-hSynI-WWOX) corrects neuronal function and, by the authors' own sentence, *"without correcting RG abnormalities"*; **A51** corrects progenitor identity and NEUN⁺ and leaves SATB2⁺/CTIP2⁺ untouched. (ii) 🔴 **A51 is identified as BTX-A51, a CK1α + CDK7 + CDK9 inhibitor** (`INFERENZA`, four convergent points) — so its "MYC inhibition" is almost certainly **CDK9-mediated RNA-Pol-II elongation suppression**, and **its Wnt direction is contested**: CK1α is the β-catenin priming kinase and an independent study reports BTX-A51 **raising** β-catenin protein. **The axis this strategy names is not the axis its only reagent isolates.** See [`a51_deconvolution_and_repurposing_20260921.md`](../analysis/a51_deconvolution_and_repurposing_20260921.md).`

**W6-C2 — `DL-THER-089` should carry the compound identity and the CNS zero.**
- **File:** `disease-models/wwox/research/discovery_ledger_current.md` · `DL-THER-089` begins **line 2331**; the
  *"Cosa è A51"* bullet is at **line 2334**
- **Exact current text (fragment):** `- **Cosa è A51:** un inibitore **multi-chinasi**, non un inibitore di MYC. Il paper stesso lo definisce *"a multi-kinase inhibitor (A51) established to suppress Wnt and MYC expression"*.`
- **Proposed addition:** `**AGGIORNAMENTO 2026-09-21 — il composto è identificato.** A51 è, con alta probabilità, **BTX-A51**: *"a first-in-class oral small molecule inhibitor of casein kinase 1α (CK1α) and cyclin dependent kinase (CDK) 7 and 9"* (`PMID 40665325`), dal gruppo **Ben-Neriah** (Hebrew University–Hadassah), la stessa istituzione del laboratorio Aqeilan e la fonte dichiarata del composto. `INFERENZA` su quattro punti convergenti; **si chiude leggendo la referenza 62 del paper o la sottosezione "MYC inhibition" di File009**. **Fase I completata negli adulti (`NCT04872166`), RP2D 21 mg 3 gg/settimana; età mediana 75; nessuna esposizione pediatrica; due tossicità epatiche DLT.** 🔴 **Zero dati CNS: `BTX-A51` restituisce 6 record in tutto PubMed e nessuno nomina brain, CNS o barriera ematoencefalica.** 🔴 **E la direzione Wnt è contestata**: CK1α è la chinasi di priming della β-catenina, e uno studio indipendente riporta che BTX-A51 **aumenta** i livelli proteici di β-catenina (`PMID 42714273`) — l'opposto di ciò che `TX-004` richiede. **Nessun triage di sicurezza eseguito; BLOCK-1 resta aperto.**`

**W6-C3 — `R-03`'s BBB row should record the measured query result, not only the assertion.**
- **File:** `disease-models/wwox/analysis/mechanism_intervention_map.md` · `R-03` table, the `**BBB_RELEVANCE**` row
- **Exact current text:** `| **BBB_RELEVANCE** | ❌ not established for the tool compounds |`
- **Proposed replacement:** `| **BBB_RELEVANCE** | ❌ not established for the tool compounds. **Measured 2026-09-21:** a targeted PubMed query for a brain-penetrant tankyrase inhibitor with brain-exposure pharmacokinetics returns **0 records** (over-conjoined query — weak evidence of absence, reported as a query result). ⚠️ **And BBB is not the gate for the next experiment**, which is in organoids: XAV939 is dish-testable today and is already the named comparator in `E-10` |`

**W6-C4 — `NS-015` can be partially closed.**
- **File:** `disease-models/wwox/research/discovery_ledger_current.md` · **line 297**
- **Exact current text (fragment):** `| NS-015 | KG esterni (Open Targets/DRKG) + AdisInsight (se autorizzato): **inibitori Wnt/tankyrase** approvati o in trial con profilo pediatrico | farmacologica | MOL-0…`
- **Proposed:** mark **partially answered** — no Wnt/tankyrase agent with a paediatric profile was surfaced by
  this node's searches, and the one clinical-stage agent actually in hand (BTX-A51) is an **adult oncology drug
  with no paediatric exposure and no CNS data**. The item stays open for the **selective CDK9** class, which
  this node did **not** census and which is now the highest-value remaining gap.

---

## 8. Source attribution

Retrieved from **PubMed**. ⚠️ **DOI provenance:** a `convert_article_ids` pass over all seven PMIDs returned
`API_ERROR`; a three-PMID batch succeeded. DOIs below come from the authoritative `identifiers.doi` field of the
in-act `get_article_metadata` responses. **One discrepancy is recorded rather than smoothed:** for
`PMID 42714273` the converter returned **the PMID alone with no DOI**, while `get_article_metadata` returned
`10.1128/jvi.01042-26`. The metadata value is used and the disagreement is stated.

| PMID | Citation | DOI |
|---|---|---|
| 42397075 | Steinberg DJ *et al.* Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids. *Brain* 2026 | [10.1093/brain/awag239](https://doi.org/10.1093/brain/awag239) |
| **40665325** | Ball BJ *et al.* Phase I first-in-human dose escalation study of the oral casein kinase 1α and cyclin dependent kinase 7/9 inhibitor BTX A51 in advanced MDS and AML. *J Hematol Oncol* 2025 · **converter-verified** | [10.1186/s13045-025-01724-z](https://doi.org/10.1186/s13045-025-01724-z) |
| 39483885 | Ball B *et al.* The same study, *Research Square* preprint 2024 | [10.21203/rs.3.rs-4954060/v1](https://doi.org/10.21203/rs.3.rs-4954060/v1) |
| 42714273 | Flor R *et al.* BTX-A51 treatment modulates host innate immune responses via NF-κB and β-catenin signaling during Rift Valley fever virus infection. *J Virol* 2026 · ⚠️ **converter returned no DOI** | [10.1128/jvi.01042-26](https://doi.org/10.1128/jvi.01042-26) |
| 39140066 | Zhang H *et al.* 2,4-Diaminopyrimidine derivatives as potent CDK7 inhibitors. *ACS Med Chem Lett* 2024 | [10.1021/acsmedchemlett.4c00040](https://doi.org/10.1021/acsmedchemlett.4c00040) |
| 41704356 | Liu M *et al.* 7-Pyrrolo[2,3-d]pyrimidine derivatives as potent CK1α inhibitors. *ACS Med Chem Lett* 2026 | [10.1021/acsmedchemlett.5c00642](https://doi.org/10.1021/acsmedchemlett.5c00642) |
| 42669983 | Waghmare PS *et al.* Casein Kinase 1 and CK2 as Therapeutic Targets in Cancer. *Mini Rev Med Chem* 2026 | [10.2174/0113895575489331260803103425](https://doi.org/10.2174/0113895575489331260803103425) |
| **34696771** | Bian E *et al.* Super-enhancer-associated TMEM44-AS1 aggravated glioma progression by forming a positive feedback loop with Myc. *J Exp Clin Cancer Res* 2021 · **converter-verified** — the MYCi975 CNS-context use | [10.1186/s13046-021-02129-9](https://doi.org/10.1186/s13046-021-02129-9) |
| 34359754 | Rea J *et al.* Novel MYC-regulated lncRNAs in Group 3 Medulloblastoma. *Cancers* 2021 — OMOMYC as a cellular tool | [10.3390/cancers13153853](https://doi.org/10.3390/cancers13153853) |
| 32562591 | Hwang S-K *et al.* *J Biochem Mol Toxicol* 2020 — 10058-F4 in glioblastoma cells | [10.1002/jbt.22552](https://doi.org/10.1002/jbt.22552) |
| 38183981 | Malik S *et al.* Antitumor efficacy of a sequence-specific DNA-targeted γPNA-based c-Myc inhibitor. *Cell Rep Med* 2024 | [10.1016/j.xcrm.2023.101354](https://doi.org/10.1016/j.xcrm.2023.101354) |

---

**End.** Not medical advice. No safety triage was run and no druggability score assigned. Read-only toward every
canonical file; nothing promoted, nothing committed.
