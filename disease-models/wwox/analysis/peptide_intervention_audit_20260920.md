# Peptide intervention audit — WWOX-dependence triage for WOREE / WWOX-DEE

**Batch:** `SCIENTIST_CHANG_NS_WWOX_NEUROPROTEOSTASIS_AND_PEPTIDE_INTERVENTION` · Wave 2 (Scientist B)
**Date:** 2026-09-20 · Non-canonical analysis file. **No canonical file edited. No commit candidate created.**
Source of all full text: **PubMed / PubMed Central** via the PubMed MCP route.

---

## 0 · Declared depth of reading — stated before any finding

| Paper | PMID | PMCID | DOI | Depth actually achieved |
|---|---|---|---|---|
| *Normal cells repel WWOX-negative or -dysfunctional cancer cells via WWOX cell surface epitope 286-299*, **Commun Biol** 2021 | **34140629** | PMC8211909 | [10.1038/s42003-021-02271-2](https://doi.org/10.1038/s42003-021-02271-2) | 🟢 **READ IN FULL** — Introduction, all Results sections, full Discussion, full Methods, supplementary-file list. 248 lines of extracted prose, 100 % read. |
| *Therapeutic Zfra4-10 or WWOX7-21 Peptide Induces Complex Formation of WWOX with Selective Protein Targets in Organs…*, **Cancers** 2020 | **32764489** | PMC7464583 | [10.3390/cancers12082189](https://doi.org/10.3390/cancers12082189) | 🟢 **READ IN FULL** — Introduction, Results §2.1–2.11, Discussion, Methods §4.1–4.10, Conclusions, Patents. 100 % read. |
| *WWOX phosphorylation…* (Wave-1 carry-over) | 31752354 | — | — | 🟡 **ABSTRACT ONLY** — unchanged from Wave 1. Quoted below only where Wave 1 already receipted it, and always marked. |

> 🔴 **Acquisition ceiling, restated and unchanged from Wave 1.**
> `eutils.ncbi.nlm.nih.gov` and `ebi.ac.uk` are policy-denied here (403 at the agent proxy); `WebFetch`
> to `pmc.ncbi.nlm.nih.gov` is `EGRESS_BLOCKED`; no PDF extractor is installed. The MCP extraction
> **strips every figure callout and reference marker**, leaving bare `()` in the prose.
> **Consequence, binding on everything below: not one claim in this file is anchored to a figure
> panel.** Where a paper's only evidence for something is a Western blot or a micrograph, this audit
> records *what the prose asserts the panel shows* and says so explicitly. Two specific adjudications
> are therefore left OPEN and marked 🔒 (WWOX protein status of MDA-MB-231 and U87-MG in the authors'
> own hands; the brain-vs-lung co-IP panel). **I did not inspect any figure and do not claim to have.**

---

## 1 · Main table

Sequences are reproduced **verbatim from the Methods**, including the authors' own N-terminal
coupling residues where they say so.

| Peptide | Sequence (as printed) | Target / node the paper names | **REQUIRES WWOX?** | Model | Dose / route / exposure | Rescue endpoint | Sign-inversion or safety flag | WOREE transferability | Verbatim quote + PMID |
|---|---|---|---|---|---|---|---|---|---|
| **WWOX286-299 "repl"** | `DYWAMLAYNRSKLC` (14 aa; Cys not declared as a coupling addition, unlike gre) | Cell-surface epitope inside the SDR domain; repels visiting WWOXd cells. Receptor on the receiving cell **never identified** | **UNCLEAR** — see § 3 | Coated plastic + MDA-MB-231; U87-MG; L929S/MDA-MB-231 coculture; EGFP-SDR stable MDA-MB-231 | **200 µM coated on dish**; or cells pretreated **20 µM, 4 h, 37 °C**, then washed; antibody 1:100 in coculture | **None.** Endpoint is direction of migration (retrograde vs anterograde) — a metastasis-homing endpoint, not any rescue of a WWOX-loss phenotype | ⚠️ **repl blockade is pro-invasive**, and repl display itself drives bystander invasion | **NONE** | *"When WWOX286-299 peptide (200 μM) was coated onto the culture dish surface, MDA-MB-231 cells strongly resisted to migrate over to the peptide-coated area"* — PMID 34140629 |
| **pY287-WWOX286-299 "pY287repl"** | `DpYWAMLAYNRSKLC` | Same epitope, Y287-phosphorylated | UNCLEAR (derivative of repl) | Coated plastic; U87-MG | 200 µM coated; coating amount **doubled** vs repl | None | ⚠️ **Sign-attenuation**: one phosphate removes ~half the activity | NONE | *"When WWOX286-299 is phosphorylated at Y287, the repellence activity of the phosphorylated peptide was significantly reduced (~50% reduction)"* — PMID 34140629 |
| **WWOX7-21 "gre"** | `CAGLDDTDSEDELPPG` (first Cys **added** for KLH coupling → the 15-mer is `AGLDDTDSEDELPPG`) | Membrane WWOX itself; Hyal-2/WWOX/SMAD4; IκBα/WWOX/ERK; pY33-WWOX | **YES — WWOX-DEPENDENT** | BALB/c + 4T1 syngeneic; coated plastic/MDA-MB-231; mouse spleen, lung, brain co-IP | **Tail vein**, schedule as for Zfra4-10 (see next row); *in vitro* 20 µM 4 h, or coated 200 µM | **None.** Endpoints: tumour volume, Z-cell activation, endogenous-WWOX co-IP. All cancer endpoints | ⚠️ **Combination inversion** (see Zfra4-10 row) | **NONE** | *"Zfra4-10 binds to membrane Hyal-2 [], and WWOX7-21 may interact with membrane WWOX (unpublished). This raises the strong scenario that both peptides drive a common signal pathway, which is Hyal-2/WWOX/SMAD4, to limit cancer growth."* — PMID 32764489 |
| **pS14-WWOX7-21 "pS14gre"** | `CAGLDDTDpSEDELPPG` | Same, S14-phosphorylated | **YES — WWOX-DEPENDENT** | Coated plastic; prior *in vivo* xenograft (cited) | 200 µM coated | None | 🔴 **HARD SIGN INVERSION.** One phosphate converts an anti-tumour peptide into a pro-tumour one, and it also blocks a chemotherapeutic | **NONE — this is a safety datum, not an efficacy datum** | *"In stark contrast, pS14-WWOX7-21 peptide strongly supports cancer growth in vivo and blocks ceritinib-mediated apoptosis in vitro."* — PMID 34140629 (Introduction, restating 31752354) |
| **WWOX7-11** | `AGLDD` (inferred from the scrambled controls `DLDGA`, `LDGDA`, `IGIDD`, `AGLEE`); `WWOX7-11A7R` active, `WWOX7-11G8R` inactive | Blocks WWOXd-induced redox rise in WWOXf cells; attracts U87-MG when coated | **UNCLEAR** — the rescue is scored **in the WWOX-expressing partner cell** | MEF `Wwox` WT vs KO coculture; U87-MG | **10 µM, 2 h**, pretreat, then wash | Abolition of the >5-fold redox rise **in the wild-type cell**, and no cell death. **The protected cell is the WWOX-positive one** | — | **NONE** (protects WWOX-positive cells from WWOX-negative ones — the inverse of the WOREE need) | *"When WWOX7-11 peptide (10 μM) was used to pretreat MEF wild type or knockout cells for 2 hr prior to washing and running the migration assay, the increased redox activity in wild type cells was abolished"* — PMID 34140629 |
| **Zfra4-10** | `NH-RRSSSCK-COOH` | Membrane **Hyal-2** → dephosphorylation of WWOX at Y33/Y61 → spleen Z-cell activation | **YES — WWOX-DEPENDENT** *(efficacy arm)*; the molecular Zfra–WWOX interaction is separately **WWOX-INHIBITORY**, see § 3.6 | BALB/c/4T1; nude/B16F10, BCC, U87-MG, 13-06-MG; NOD-SCID | **2 mM in 100 µL PBS, tail vein, every other day ×3 in one week**, rest 2 weeks, then tumour inoculation. Also **1 mM in 100 µL sterile MilliQ water ×3**, and **4 mM in 100 µL ×3 weeks**. *In vitro* Z-cell activation **20 µM, 24 h** | **None neuronal.** Tumour volume, lung metastasis, Z-cell killing of 4T1 | 🔴 **COMBINATION INVERSION** (see § 4.1) · ⚠️ prophylaxis-only · ⚠️ buffer-dependent activity | **NONE** | *"Zfra4-10 binds to membrane Hyal-2, induces dephosphorylation of WWOX at pY33 and pY61, and drives Z cell activation for the anticancer response."* — PMID 32764489 (Abstract, repeated verbatim in Discussion) |
| **Zfra1-31** | `NH-MSSRRSSSCKYCEQDFRAHTQKNAATPFLAN-COOH` | Same pathway; self-polymerises via **Ser8** | **YES — WWOX-DEPENDENT** (same pathway) | Nude mice / B16F10 | **Tail vein once per week ×3 weeks**, rest 1 week, then inoculation | Tumour volume ↓78 ± 8 % (n = 5) | S8G control abolishes activity (a proper negative control) | NONE | *"Zfra suppressed B16F10 growth by 78 ± 8% (= 5) in nude mice"* — PMID 32764489 |
| **Zfra(S8G)** | S8→G8 point mutant | — | n/a (inactive control) | nude/BCC | as above | none | Clean loss-of-function control: *"Alteration of S8 to G8 abolishes the anticancer function of Zfra"* | n/a | *"Zfra-treated nude mice resisted the growth of BCC cells, compared to PBS controls and Zfra(S8G) mutant peptide"* — PMID 32764489 |
| *(non-peptide, same therapeutic set)* **pY33-WWOX antiserum** | — | Endogenous pY33-WWOX | **YES — WWOX-DEPENDENT by construction** | nude/BCC, NOD-SCID | 10 µL serum + 90 µL PBS, tail vein ×3 | Tumour growth (alone: weak) | Alone weaker than Hyal-2 IgG; **with Zfra4-10 it completely blocked BCC** — a positive combination, in contrast to the peptide+peptide pair | NONE | *"pY33-WWOX antibody was less effective in blocking BCC growth than Hyal-2 antibody… Notably, Zfra4-10 peptide and pY33-WWOX antiserum, in combination, completely blocked the growth of BCC"* — PMID 32764489 |
| *(non-peptide)* **Hyal-2 antiserum** | — | Membrane Hyal-2, upstream of WWOX | **YES** — the paper's own mechanism routes it through WWOX | nude/BCC; NOD-SCID/B16F10 | 10 µL serum + 90 µL PBS, tail vein ×3 | Tumour growth, **>75 % inhibition** | — | NONE | *"The growth of skin basal cell carcinoma (BCC) tumor was blocked in mice receiving Zfra peptide or Hyal-2 antiserum (>75% inhibition)"* — PMID 32764489 |
| *(non-peptide)* **Sonicated hyaluronan HAson3/6/8** | — | Hyal-2 agonist → Hyal-2/WWOX | **YES** (as framed) | BALB/c, NOD-SCID; B16F10, 4T1, MDA-MB-231 | 2 mg/mL HA sonicated 3/6/8 h, **tail vein once per day ×3 days**, or ×3 weeks | Tumour growth | ⚠️ UV-fragmented HA inert; native high-MW HA **promotes** cancer growth — a size/processing-dependent sign flip | NONE | *"Taken together, sonicated HA and specific antibodies against Hyal-2 act as agonists in stimulating membrane Hyal-2 in Z cells, so as to suppress cancer growth."* — PMID 32764489 |

---

## 2 · Tested in a WWOX-deficient model?

**Wave 1's claim is CONFIRMED and can now be stated at full-text depth for both papers: no peptide in
either paper was ever administered to a WWOX-null animal.** What the two papers actually did:

| Peptide | Ever given to a `Wwox−/−` **animal**? | Ever applied to a genotype-defined WWOX-deficient **cell**? | Evidence |
|---|---|---|---|
| **Zfra4-10** | **NO** | **NO** | Every *in vivo* arm in PMID 32764489 is BALB/c, nude (`BALB/cAnN.Cg-/CrlNarl`) or NOD-SCID — all WWOX-intact. The only `Wwox`-genotype animal in the paper is a **heterozygote used as a donor of spleen cells**, not as a host: *"In a similar experiment, activated Z cells were isolated from heterozygous Wwox+/− mice and attacked 4T1 cells"* (PMID 32764489). The peptide-treated animals are explicitly wild type: *"Naïve wild type Wwox B6 mice were treated with Zfra (1 mM in 100 μL PBS) once via tail vein injection"* (PMID 32764489). |
| **Zfra1-31** | **NO** | NO | Nude mice only. |
| **WWOX7-21 / gre** | **NO** | **NO** | Same BALB/c cohorts in PMID 32764489; coated-plastic and MDA-MB-231 pretreatment in PMID 34140629 (cell WWOX status 🔒 not resolvable in prose). |
| **pS14-WWOX7-21** | **NO** | NO | Coated plastic only in PMID 34140629; the *in vivo* growth-enhancement result is cited to 31752354 (abstract-only here). |
| **WWOX286-299 / repl** | **NO** | **NO — and the one experiment that could have settled it was not done.** | Peptide-to-cell-surface binding was tested **only on WWOX-positive cells**: *"When live MEF wild type cells were incubated with WWOX7-21 or WWOX286-299 peptide at 4° C for 30 min followed by washing and processing immunostaining, these peptides colocalized with TβRII on the cell surface"* (PMID 34140629). The `Wwox` **knockout** MEFs were available in the very same experiment set and were **not** used for this binding assay. |
| **WWOX7-11** | **NO** | 🟡 **PARTIAL — the only exposure of a `Wwox`-null cell to a peptide anywhere in these two papers**, and the readout is in the wild-type partner: *"pretreat MEF wild type **or** knockout cells… the increased redox activity **in wild type cells** was abolished"* (PMID 34140629). The "or" is the authors'; the design does not separate which cell carried the peptide, and no endpoint is scored in the knockout cell. |
| **Hyal-2 IgG / pY33-WWOX IgG / HAson** | **NO** | NO | nude, NOD-SCID, BALB/c only. |

**So the corpus-level gap Wave 1 identified is not an accident of one paper.** PMID 34140629 uses
`Wwox` knockout MEFs in at least eight separate experiments (migration, redox, UV/BCD, calcium influx,
TβRII IgG, FRET signalling, TGF-β1 stress fibres) and PMID 32764489 has `Wwox+/−` mice in hand — and
across both papers the **therapeutic peptides are never scored for efficacy in the WWOX-deficient
genotype.** The knockout is used exclusively as the *aggressor* or the *disease model of cancer*,
never as the *patient*.

---

## 3 · Bucket assignment, with the reasoning that forced it

### 3.1 `WWOX7-21` / gre → **WWOX-DEPENDENT**
Four independent mechanistic statements, all readouts on endogenous WWOX, none of which has meaning at
zero WWOX:

- *"WWOX7-21 may interact with membrane WWOX (unpublished)"* — PMID 32764489. **The authors' own
  proposed receptor for this peptide is WWOX itself, and it is unpublished.**
- *"Mice, receiving either Zfra4-10 or WWOX7-21 peptide, had increased binding of WWOX with C1qBP,
  CD133, p21, JNK1, COX2, p-ERK, Foxp3, and p53 in the spleen"* — PMID 32764489. The paper's entire
  pharmacodynamic readout is co-immunoprecipitation **of endogenous WWOX**.
- *"Loss of the binding between WWOX and target proteins leads to increased cancer cell growth."* —
  PMID 32764489.
- Wave 1's abstract-level finding (PMID 31752354) — *"significant upregulation of pY33-WWOX"* and
  *"disruption of the IκBα/WWOX/ERK prosurvival signaling"*, restated verbatim in the Introduction of
  PMID 34140629 — is now corroborated by full text rather than abstract.

**The title of PMID 32764489 is accurate about its own mechanism, and that is exactly the problem.**
"Induces Complex Formation of WWOX with Selective Protein Targets" is a mechanism defined on a protein
WOREE patients do not have. A peptide whose measured effect is *how much endogenous WWOX binds its
partners* has, by construction, no effect where endogenous WWOX is absent.

### 3.2 `pS14-WWOX7-21` → **WWOX-DEPENDENT**, and a safety exhibit
Same node, opposite sign. *"In stark contrast, pS14-WWOX7-21 peptide strongly supports cancer growth
in vivo and blocks ceritinib-mediated apoptosis in vitro."* (PMID 34140629). PMID 34140629 adds a
second, independent inversion for the same phospho-pair: *"the S14-phosphorylated gre peptide,
designated pS14gre or pS14-WWOX7-21, lost its enhancing activity for cell migration as compared to
controls"*. One phosphate, two assays, two reversals.

### 3.3 `WWOX286-299` / repl → **UNCLEAR**, and the title's ambiguity resolves **against** WOREE relevance

The batch brief asked the decisive question: does the 286-299 epitope act **ON** WWOX-negative cells,
or is it merely **SECRETED BY / DISPLAYED BY** WWOX-positive cells? **The answer from full text is:
it is displayed by WWOX-positive cells and it acts on WWOX-deficient cells — but the therapeutic
vector points the wrong way for WOREE, and the receiver's WWOX-dependence is untested.**

The paper's own conclusion on the physiological mechanism is unambiguous and is **WWOX-DEPENDENT in
the emitting cell**:

> *"Together, cell surface-exposed SDR domain in WWOX is responsible for repelling migrating WWOXd
> cells such as metastatic cancer cells. In other words, WWOXd metastatic cancer cells would face
> repellence in homing to a normal organ possessing WWOXf cells with membrane repl epitope."*
> — PMID 34140629

The therapeutic logic of the whole paper is therefore: **use the normal, WWOX-intact compartment's
epitope to fend off the WWOX-deficient compartment.** In WOREE there is no WWOX-intact compartment —
every cell is WWOXd. The paper's own model has nothing to say about a host in which the repelling
population does not exist.

The **synthetic** repl peptide is a separate question, and it is the one genuinely open item here. The
coated-peptide experiment does act on the receiving cell without any cell displaying WWOX:
*"MDA-MB-231 cells strongly resisted to migrate over to the peptide-coated area"* (PMID 34140629).
If MDA-MB-231 were WWOX-null, this would be a WWOX-independent peptide action. **It cannot be
adjudicated here**, for two reasons stated by the paper itself:

- 🔒 The WWOX status of the WWOXd panel is shown only in a Western blot I cannot inspect:
  *"The protein expression profiles for WWOX, TβRII…, Hyal-2, ERα… in many tested WWOXd and WWOXf
  cells are shown by Western blots (Supplementary Fig.)"* — PMID 34140629.
- The paper's own definition forbids inferring null status from the "WWOXd" label:
  *"WWOXd cells may express abundant mutant WWOX protein or nothing at all."* — PMID 34140629.
  And concretely: *"B16F10 cells, a WWOXd cell line, express WWOX."* — PMID 34140629.

**Verdict: UNCLEAR, with an explicit route to closing it** — a repl-coating migration assay on
`Wwox−/−` MEFs (which the lab has) versus `Wwox+/+` MEFs would settle it in one experiment, and was
not performed.

### 3.4 `WWOX7-11` → **UNCLEAR**, and pointed the wrong way
The only peptide in either paper with a protective endpoint, and the protected cell is the
**WWOX-positive** one. *"The observations suggest that WWOX7-11 peptide supports cell survival via
blocking increased redox activity."* (PMID 34140629) — the survival is that of the wild-type MEF
under attack from the knockout MEF. Transferring this to WOREE would require the inverse experiment
(protect the WWOX-null cell), which is not in the paper.

### 3.5 `pY287repl` → **UNCLEAR**, derivative
*"Stimulation of EGFP-SDR cells with pY287-WWOX (or pY287repl) antibody could not convert the
retrograde into anterograde migration in control cells (), suggesting that Y287 phosphorylation is
not involved in the cell repellence."* — PMID 34140629. Note that this sits alongside the coated-peptide
result showing pY287repl **does** lose ~50 % repellence, which the authors attribute to
matrix-binding rather than signalling. The two are reconcilable but the paper does not reconcile them.

### 3.6 `Zfra4-10` / `Zfra1-31` → **WWOX-DEPENDENT** for the therapeutic arm, **WWOX-INHIBITORY** at the molecular level

This peptide genuinely splits, and PMID 32764489 documents both halves.

**Efficacy arm — WWOX-DEPENDENT.** *"Zfra4-10 binds to membrane Hyal-2, induces dephosphorylation of
WWOX at pY33 and pY61, and drives Z cell activation for the anticancer response."* (PMID 32764489).
Every step after the receptor is a WWOX phospho-state. *"Zfra significantly suppressed the expression
of Hyal-2 and phosphorylation of WWOX at Y33 and Y61 (>90%)… in the spleen"* — the pharmacodynamic
marker is WWOX. At zero WWOX there is no Y33, no Y61, no S14 and no Hyal-2/WWOX/SMAD4 complex.

**Molecular arm — WWOX-INHIBITORY.** The paper's §2.3 heading says it outright, and this is a
**refinement of Wave 1**, which had zfration as target-agnostic chemistry:

> *"Zfra binds to WWOX at both the-terminal WW domain and the-terminal short-chain alcohol
> dehydrogenase/reductase (SDR) domain and suppresses WWOX phosphorylation at Tyr33 and its apoptotic
> function"* — PMID 32764489
> *"Zfra restricts the functions of nuclear factor NF-κB, JNK1 kinase, and tumor suppressors p53 and
> WWOX"* — PMID 32764489
> *"These complexes are resistant to dissociation by β-mercaptoethanol under reducing SDS-PAGE,
> suggesting that Zfra covalently binds to WWOX and other protein targets, leading to rapid
> degradation []. The degradation is ubiquitin- and proteasome-independent."* — PMID 32764489

**WWOX is a substrate of zfration.** Wave 1 was right that zfration is chemistry that runs without
WWOX present; Wave 2 adds the direction: **when WWOX *is* present, zfration destroys it.** For a
genotype with residual hypomorphic WWOX protein — which several WWOX-DEE alleles are — Zfra is
directionally *harmful*, not merely inert. For a true null it is simply mechanism-less.

---

## 4 · The safety findings, which outrank the efficacy findings

### 4.1 🔴 Combination inversion — two peptides that each suppress cancer **enhance** it together
This is the single hardest safety datum in the batch and it is reported independently in **both** papers.

> *"In contrast, when mice received both Zfra4-10 and WWOX7-21 peptides, the anticancer effect from
> both peptides were totally lost (D)."* — PMID 32764489
> *"However, in mice receiving both Zfra4-10 and WWOX7-21 peptides, WWOX had reduced binding with the
> target proteins down to a basal level (B), and cancer growth was significantly increased (A,D)."*
> — PMID 32764489
> *"Compared to controls, Zfra4-10 or WWOX7-21 peptide significantly suppressed cancer growth. **In
> combination, both peptides enhanced cancer growth.**"* — PMID 34140629

The proposed cause is direct covalent neutralisation: *"Zfra4-10 reciprocally neutralizes WWOX7-21
function in cancer suppression. The neutralization is probably due to covalent binding of both
peptides."* (PMID 32764489). A therapeutic class in which two members, each efficacious alone, are
**net-harmful in combination** via covalent self-reaction carries a combinatorial risk surface that no
dose-finding protocol in these papers addresses.

### 4.2 🔴 Phospho-state inversion — `pS14-WWOX7-21`
See § 3.2. Restated here because it is a safety datum, not an efficacy datum.

### 4.3 ⚠️ The active species is an uncontrolled polymer whose activity depends on the buffer
Two statements in PMID 32764489 that do not sit comfortably together:

> *"The failure is due, in part, to over self-polymerization of Zfra or its conjugation with blood
> proteins that results in loss of the anticancer efficacy in vivo []."*
> *"Conceivably, over self-polymerization of Zfra caused by PBS leads to its functional inactivation…"*
> *"In this study, Zfra was resuspended in water, and its anticancer activity was reduced due to
> insufficient self-polymerization []."*

PBS over-polymerises it; water under-polymerises it. The Methods respond with a hand-manufacturing
protocol — *"Each tube was flushed with nitrogen to prevent oxidation of serines in Zfra peptides"*,
*"peptides were freshly diluted at 1–4 mM in 100 μL degassed PBS and used for injection immediately
to prevent over self-polymerization"* — which is a CMC red flag: the drug substance is defined by how
fast you inject it after dilution.

### 4.4 ⚠️ Zfra works only prophylactically
> *"However, when ongoing solid tumors are under establishment in mice, Zfra cannot effectively
> suppress the tumor cell growth []."* — PMID 32764489

Every efficacy schedule in PMID 32764489 doses **before** tumour inoculation (peptide → rest 1–2 weeks
→ inoculate). WOREE is established in utero. A prevention-only agent has no mapping onto a
congenital loss-of-function disease.

### 4.5 ⚠️ Blocking repl is pro-invasive, and repl display drives bystander invasion
> *"pretreatment of L929 cells with repl antibody or TGF-β1 resulted in significant increases in the
> numbers of MDA-MB-231-EGFP cells in the L929 cell areas"* — PMID 34140629
> *"When MDA-MB-231-EGFP-SDR cells were seeded over the top of control MDA-MB-231 cells in the apical
> chamber, control MDA-MB-231 cells acquired an enhanced invasion activity by ~2–3-fold"* — PMID 34140629

The second is the more interesting one: **the repellence mechanism itself pushes neighbouring cells
into the matrix.** A surface-displayed repellent is not a one-signed therapeutic.

### 4.6 The toxicity statements are bare assertions
> *"These synthetic peptides were not cytotoxic to cells in vitro, as determined by cell cycle
> analysis. Also, the peptides are not toxic to mice."* — PMID 34140629 (no data location given in prose)
> *"Zfra is not toxic and does not cause damage to organs, implying its therapeutic potential."*
> — PMID 32764489 (Introduction, cited to prior work)

No histopathology, no weight curve, no haematology, no dose-limiting toxicity, no repeat-dose study
appears in either paper. **"Not toxic" here is a sentence, not a dataset.** Record it as such.

---

## 5 · Blood–brain barrier / CNS exposure — these papers do better than Wave 1's "do not exclude the possibility", and the answer is negative

Wave 1 had only the authors' hedge. PMID 32764489 supplies **two concrete, independent negatives**.

**(a) Biodistribution: the peptide goes to the spleen, not to other organs.**
> *"The injected Zfra peptides in circulation become polymerized, exhibit self-fluorescence, and are
> mainly trapped or filtered in the spleen but not in other organs []."* — PMID 32764489

**(b) 🔴 The decisive one — the paper's own target-engagement readout FAILED IN THE BRAIN.**
The pharmacodynamic marker of both peptides is peptide-induced complex formation of endogenous WWOX.
It was measured in spleen, lung and brain. It worked in spleen and lung. It did not work in brain:

> *"Under similar conditions, endogenous WWOX strongly bound to Iba1, Oct4, ERK1/2, NF-κB p65, GFAP,
> and p53 in the lung of mice treated with Zfra4-10 or WWOX7-21 peptide (C). **The binding did not
> occur in the brain (C).**"* — PMID 32764489 (Results §2.4)

Restated in the Discussion in the authors' own summary voice:

> *"Similarly, Zfra4-10 or WWOX7-21 peptide enhances the binding of WWOX with Iba1, GFAP, Oct4,
> ERK1/2, p53, and NF-κB p65 in the lungs of BALB/c mice. **However, the binding is barely detectable
> in the brain.**"* — PMID 32764489

This is a negative CNS pharmacodynamic result **in the authors' own hands, after systemic tail-vein
dosing, using their own chosen mechanism marker.** It does not measure BBB permeability directly —
it measures something more decisive for therapy, namely whether the drug's mechanism fires in brain
tissue. It did not.

🔴 **Internal inconsistency to record.** The Abstract and the Conclusions of PMID 32764489 both say
the induced binding occurred *"in the spleen, brain, and/or lung"* — the Abstract verbatim:
*"an increased binding of endogenous tumor suppressor WWOX with ERK, C1qBP, NF-κB, Iba1, p21, CD133,
COX2, Oct4, and GFAP in the spleen, brain, and/or lung which led to cancer suppression"*. The Results
say the brain binding **did not occur**. The `and/or` construction in the abstract is doing work the
data do not support; a reader who stops at the abstract — or at a search snippet — will carry away the
opposite of the result. The only brain-positive item in Results is a presenilin-1 fragment with **no
stated treatment dependence**: *"WWOX bound to a degradation product of presenilin-1 of 17 kDa in the
brain and lung"*, and the full-length form was negative in every arm including PBS: *"binding of WWOX
with presenilin-1 (60 kDa) did not occur in the brains of mice treated with PBS, or Zfra4-10 and/or
WWOX7-21 peptides"*. 🔒 The underlying panel is a Western blot I cannot inspect; this adjudication
rests entirely on the two prose sentences quoted above, which agree with each other.

**Note the geography is not the obstacle.** The machinery is in the brain — *"Other organs such as
brain and small intestine also have the WWOX/Hyal-2/TβRII complex."* (PMID 34140629). The target is
there; the drug effect is not.

---

## 6 · The six-claim discipline applied to "surface epitope"

The batch brief required these six to be kept apart. Here is where PMID 34140629 actually lands:

| Claim | Status in PMID 34140629 | Evidence class |
|---|---|---|
| **1 · PRESENCE** of the epitope in the WWOX sequence | Asserted, trivially true | sequence |
| **2 · Extracellular ACCESSIBILITY** | **Asserted, not independently demonstrated in this paper.** *"Membrane-bound WWOX possesses two cell surface epitopes, namely amino acid #7–21 (WWOX7-21) and #286–299 (WWOX286-299)"* — stated as background. The supporting experiment here is that **exogenous peptide** added to live WT cells at 4 °C colocalises with TβRII — which shows the *peptide* binds the surface, not that the *endogenous epitope* is exposed | immunofluorescence on WT cells only |
| **3 · FUNCTION** (repellence / greeting) | **Demonstrated** for the synthetic peptides, in migration assays | coated-plastic + coculture migration |
| **4 · SIGNALLING** | **Partially demonstrated, and entirely in transient overexpression.** The IκBα/ERK/WWOX FRET result required *"transiently overexpressed with ECFP-IκBα, EGFP-ERK, and DsRed-WWOX"* | FRET on overexpressed constructs |
| **5 · INTERNALISATION** | **Asserted, cited to prior work.** *"TGF-β1 induces the internalization of membrane WWOX, Hyal-2 and TβRII in normal WWOXf cells"* | citation |
| **6 · Therapeutic RESCUE of a WWOX-loss phenotype** | ❌ **ABSENT.** Not attempted, not claimed, nowhere in either paper | — |

There is no step in this ladder that reaches protein replacement, and nothing in either paper is
evidence that a surface epitope peptide can substitute for a missing intracellular WWOX function.
**Do not let "cell surface epitope" migrate into "extracellular target" or "replacement route".** The
epitope's demonstrated job is cell-to-cell *recognition during metastasis*.

---

## 7 · What survives for WOREE

**Nothing survives as a therapeutic candidate. Not one peptide, not one antibody, not HAson.**

That is the finding, and it is a useful one. Five independent reasons, each sufficient on its own:

1. **Mechanism.** Every mechanism the authors propose terminates in a WWOX phospho-state or a WWOX
   protein complex — `pY33`, `pY61`, `pS14`, `pY287`, Hyal-2/WWOX/SMAD4, IκBα/WWOX/ERK, or
   "complex formation of WWOX with selective protein targets". In biallelic loss of function there is
   no WWOX to phosphorylate, dephosphorylate, or complex. The two peptides whose receiver-side
   dependence is genuinely untested (`repl`, `WWOX7-11`) have no rescue endpoint of any kind.
2. **CNS.** The authors' own target-engagement readout was negative in brain (§ 5), and the peptide
   distributes to spleen. There is no CNS pharmacology here to transfer.
3. **Endpoints.** Every endpoint in both papers is a **cancer** endpoint — tumour volume, lung
   metastasis, retrograde migration, Transwell invasion, Z-cell killing of 4T1. There is **no seizure
   endpoint, no neuronal survival endpoint, no myelination endpoint, no developmental endpoint, no
   behavioural endpoint** anywhere in either paper. Neuroblastoma lines (SH-SY5Y, NB69) appear only as
   entries in a UV bubbling-death screening panel; no peptide was tested on them for rescue. **A
   cancer endpoint is not a neuronal endpoint and cannot be read as one.**
4. **Direction.** Where a protective effect exists (`WWOX7-11`), it protects the **WWOX-positive** cell
   from the WWOX-negative one. The whole conceptual frame of PMID 34140629 — normal cells repelling
   WWOX-deficient cells — casts the WWOX-deficient cell as the *adversary to be expelled*. WOREE needs
   the opposite: rescue of the WWOX-deficient cell.
5. **Genotype.** No peptide has ever been given to a WWOX-deficient animal (§ 2), in a lab that owns
   both `Wwox−/−` and `Wwox+/−` mice and used the knockout MEFs in eight other experiments in the
   very same paper.

**And two positive safety liabilities to carry forward rather than discard:** the `pS14` phospho-state
inversion and the `Zfra4-10 + WWOX7-21` combination inversion. Both say that this chemical class has
*sign-labile* pharmacology — small covalent or phospho perturbations flip efficacy to harm. For a
paediatric neurodevelopmental indication that is a disqualifying property independent of mechanism.

**What is worth keeping, and it is not therapy:**

- **A validated reagent set**, if the lab ever needs to assay membrane WWOX: rabbit antisera against
  `gre`, `pS14gre`, `repl`, `pY287repl`, each with peptide-blocking specificity controls
  (PMID 34140629, Methods), plus anti-Hyal-2 #211–226 / #227–241 and anti-pY216-Hyal-2 (PMID 32764489).
- **One negative result of genuine value to the model**, already recorded in § 5: systemic peptide
  dosing does not engage WWOX-dependent mechanism in brain. Any future CNS-directed WWOX-axis agent
  inherits that as a prior, not as an open question.
- **One clean, cheap experiment the field has not done**, stated so it can be proposed rather than
  assumed: repl-coating migration assay on `Wwox−/−` versus `Wwox+/+` MEFs, which would convert the
  `repl` UNCLEAR into a decision (§ 3.3).

---

## 8 · Change log against Wave 1

| Wave 1 position | Wave 2 status after full text |
|---|---|
| `WWOX7-21` WWOX-DEPENDENT, from abstract of 31752354 | ✅ **CONFIRMED at full-text depth**, now with the authors' own admission that its receptor is *"membrane WWOX (unpublished)"* (PMID 32764489) |
| `WWOX286-299 / pY287` — "unread" | ✅ **READ.** Bucket **UNCLEAR**; the title's ambiguity resolves as *displayed by WWOX-positive cells, acting on WWOX-deficient cells*, with the receiver's WWOX-dependence never tested |
| Zfra zfration = WWOX-INDEPENDENT chemistry | 🔧 **REFINED, not overturned.** Still target-agnostic chemistry, but **WWOX is one of its substrates** — so in a genotype with residual WWOX protein Zfra is directionally harmful, not inert (§ 3.6) |
| Zfra *in vivo* package = WWOX-DEPENDENT | ✅ **CONFIRMED**, with the full mechanistic chain and dose/route now in hand |
| "Never tested in a WWOX-deficient animal" | ✅ **CONFIRMED for both papers**, with the `Wwox+/−` donor-spleen experiment identified as the closest approach and shown to be a donor, not a host (§ 2) |
| BBB: authors "do not exclude the possibility" | 🔼 **UPGRADED to a concrete negative** — brain target-engagement failed while lung and spleen succeeded (§ 5) |
| `pS14` sign inversion | ✅ **CONFIRMED**, plus a **second, independent inversion** found: the Zfra4-10 + WWOX7-21 combination (§ 4.1) |

---

*Attribution: full texts retrieved from **PubMed / PubMed Central**.
PMID 34140629 — [10.1038/s42003-021-02271-2](https://doi.org/10.1038/s42003-021-02271-2).
PMID 32764489 — [10.3390/cancers12082189](https://doi.org/10.3390/cancers12082189).
Nothing in this file is medical advice; it is a therapeutic-transferability audit for a disease model.*

---

## 🔴 ADDENDUM — 2026-09-21: an independent laboratory, in neurons, reports that **inhibiting** WWOX is the protective move

This audit established the sign for `Zfra1-31` from inside the originating laboratory: **zfration
takes WWOX as a substrate, so in a genotype with residual WWOX protein Zfra is directionally
harmful, not inert** (§ 3.6). That finding now has **outside confirmation**, and it arrives in the
one context that matters here — **neurons**.

**`PMID 35984507`** — Carvalho C, Correia SC, Seiça R, Moreira PI 2022, *Cell Mol Life Sci*
79(9):487, [DOI](https://doi.org/10.1007/s00018-022-04508-7), Center for Neuroscience and Cell
Biology / CIBB, **University of Coimbra** — a laboratory with no connection to NCKU. Its **title is
its finding**:

> *"**WWOX inhibition** by Zfra1-31 **restores** mitochondrial homeostasis and viability of neuronal
> cells exposed to high glucose."*

From the abstract: Zfra1-31 is described as *"**the specific inhibitor of WWOX**"*; *"high glucose
increased the levels of **activated WWOX**"*; *"the **activation of WWOX preceded** mitochondrial
dysfunction and cell death"*; *"the **inhibition of WWOX with Zfra1-31 reversed**, totally or
partially, the alterations promoted by high glucose"*. There is an in-vivo correlate: *"brain
cortical and hippocampal homogenates from young (6-month old) diabetic GK rats showed increased
levels of activated WWOX compared to older GK rats"*.

**What this does to the audit's conclusions.** It does not change any of them. It **hardens** the
one that matters most, and moves it out of the originating laboratory:

| Before | After |
|---|---|
| Zfra is directionally harmful in a WWOX-residual genotype — **inferred from the Chang lab's own chemistry** | Same conclusion, now **independently corroborated in differentiated neuronal cells, with an animal correlate**, by a group using the reagent as an **inhibitor of WWOX** and saying so in the title |

🔴 **And it completes a three-line convergence that is the strongest structural result of this
session.** Every therapeutic candidate this literature has produced acts by **antagonising WWOX**:

1. **The pTyr33-WWOX peptide** (`PMID 18371080`, `FT-109`, packet `A6`) — *"activated WOX1 plays an
   essential role in the MPP+-induced neuronal death"*; the dominant negative *"abolished this
   event"*. The peptide protects by blocking, not by substituting.
2. **The C1q→WOX1 axis** (`PMID 19484134`, `FTR-20260921-19484134-01`) — the authors' own neuronal
   extrapolation is *"There is a strong possibility that C1q activates WOX1 in neurons, which
   ultimately leads to cell death."*
3. **Zfra1-31** — this paper, **from outside the laboratory that invented the reagent, in neurons**.

**A WWOX antagonist has nothing to antagonise in a WWOX-deficient brain**, and in a compound
heterozygote carrying a missense allele that still produces protein, removing that residual protein
is the **opposite** of the therapeutic goal. **This is a category objection, not a dosing one: it is
not fixed by a different schedule, a different route or a BBB-penetrant formulation.**

⚠️ **Honesty about what this addendum is.** It rests on an **abstract**, not a reading. The full
text is unobtainable here — `PMC11071800` resolves and returns a **zero-length body** — so the paper
is filed as packet item **`A9`**, at the top of the list, precisely so that it is *read* rather than
*cited*. The specific things that could still change the picture are named there: whether any
**genetic** WWOX manipulation exists alongside the peptide (Zfra is covalent and promiscuous, so
*"Zfra protects"* and *"less WWOX protects"* are not the same claim), and whether **total** WWOX or
only **pTyr33**-WWOX moves.

**Nothing in this addendum is medical advice.**
