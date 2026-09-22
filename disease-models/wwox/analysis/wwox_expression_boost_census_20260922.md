# WWOX EXPRESSION-BOOST CENSUS — what is known to raise WWOX, and what it would mean in a neuron

> **Non-canonical research artefact.** Read-only toward every canonical file. No registry, ledger,
> queue or `*_current.md` was edited; no `BATCH_COMMIT` was run. Produced by **Scientist R**,
> 2026-09-22, in response to the reopening of the non-allele-specific upregulation axis by
> [`CC-20260922-NMD-PREMISE-WITHDRAWAL-01`](../research/commit_candidates/CC-20260922-NMD-PREMISE-WITHDRAWAL-01.md).
>
> **Public edition.** Disease-level reasoning about the **reference genotype class** (a destabilising
> SDR missense allele + a canonical splice-acceptor allele), never an individual.
> **Nothing here is medical advice.** This is an evidence census, not a treatment plan.
> **FLAG FIRST — nothing below is scored.** No agent is ranked, promoted or recommended.

---

## 0 · The question, and why it is being asked today

`therapeutic_hypotheses_ledger_current.md:216` (`HYP-20260709-02`) closed non-allele-specific WWOX
upregulation on this sentence, verbatim:

> *«L'allele di sito accettore del genotipo di riferimento (c.1057-2A>G) produce trascritto aberrante
> **destinato a NMD**: up-regolarlo spinge solo più trascritto verso la degradazione, senza proteina
> utile.»*

That premise was **withdrawn today**. Under the surviving splice outcome there is no PTC, so a boost
would raise output from **both** alleles rather than predominantly one. The axis is live again —
**and it had never been surveyed, because it was closed before anyone looked.**

This document surveys it. It reaches a negative verdict, and the negative is the finding.

---

## 1 · REPOSITORY SWEEP — what LEGEND already holds

### 1.1 · The four places the axis is closed, and they are **not** the same closure

| Locus | What it says | Load-bearing premise | Status after today |
|---|---|---|---|
| `therapeutic_hypotheses_ledger_current.md:216` (`HYP-20260709-02`) | NMD destroys the acceptor-allele transcript ⇒ a boost amplifies **only** the missense allele | 🔴 **untagged, uncited NMD clause** | **WITHDRAWN today.** The asymmetry argument collapses |
| `dismissal_ledger_current.md:101` (`DIS-003`) | *"increasing transcription/translation does not help"* | ✅ `PREMISE: DATO` — Johannsen 2018, **normal transcript, protein absent**, in fibroblasts **homozygous for Gln230** | 🟡 **HOLDS for the missense allele only.** Its own `REVIVAL_TRIGGER` is *"if it emerged that a **compound-heterozygous** transcript behaves differently from the Johannsen homozygote"* — which is exactly the configuration the withdrawal opens |
| `mechanism_intervention_map.md:660` (`N-05`) | *"the target is not the bottleneck"* **plus** the allele-asymmetry argument | half `DATO` (Johannsen), half the withdrawn NMD clause | 🟡 **Half survives.** The bottleneck argument stands; the asymmetry half does not |
| `therapeutic_strategies_current.md:58` (`TX-002`) | *"CRISPRa / endogenous WWOX transcriptional boost — **PARKED, not refuted**"*; `MATCH 1 · EVID 1 · TIME→patient 0` | same | unchanged — it was parked, not closed |

🔴 **The single most important structural fact in this sweep:** the withdrawal removes the **acceptor-allele**
half of the closure and leaves the **missense-allele** half intact. `DIS-003` is not revived by
the withdrawal — it is *narrowed*. What reopens is a question nobody had: **does the acceptor allele,
if it makes a near-full-length 412-aa protein, respond to a boost?** No datum in this repository or in
the literature addresses it.

### 1.2 · The three documented levers on endogenous WWOX the repo already carries

From `therapeutic_hypotheses_ledger_current.md:214`, verbatim:

> *«tre leve indipendenti documentate su WWOX endogeno — **miR-153** (repressore, 3'UTR), contesto
> **Kozak rs11545028** (l'allele T, −5 dall'ATG, **abbassa** traduzione: luciferasi p<0.05 in 3 linee,
> qPCR, IHC p=0.022, eQTL GTEx), sito **Sp1/Sp3 rs11644322** (introne 8; allele G lega Sp1 più forte
> → più WWOX; EMSA + supershift). Tutte agiscono sul **trascritto endogeno, non allele-specificamente**.»*

**None of the three is an agent.** Two are germline polymorphisms — facts about *variance between people*,
not levers anyone can pull. Only the first (miR-153) has a corresponding molecule, and it is already
flagged 🔴 red.

### 1.3 · The Sp1 precedent — the specificity standard this census is held to

`paper_registry_current.md:6535` (`PAPER 050`, Schirmer 2016, PMID 26857392 / PMC4859408 /
[DOI](https://doi.org/10.1093/jnci/djv387)), verbatim:

> *«**Segnale su Sp1:** l'allele G lega Sp1/Sp3 più forte → più WWOX (EMSA + supershift + siRNA).
> ⚠️ **Non un candidato terapeutico**: quasi tutti i modulatori di Sp1 disponibili lo **inibiscono**
> (direzione sbagliata), e Sp1 controlla migliaia di geni.»*

**Two independent kill criteria in one sentence: wrong direction, and a shotgun.** Section 4 applies
exactly this test to every agent class below.

### 1.4 · The anti-miR arm, already closed twice on two different grounds

- `therapeutic_hypotheses_ledger_current.md:231` — `HYP-20260709-03` (anti-miR-153):
  🔴 **red**, *«Non è WWOX-specifico… miR-153 ha molti altri bersagli documentati (PTEN, AKT) → un
  antagomiR è pleiotropico»*; kept *«perché **dimostra il principio** … non perché sia la molecola»*.
- `discovery_ledger_current.md:1815` — `DL-MECH-069b`, on the miR-186-5p site, verbatim:
  > *«**Perché un antagomiR NON è un candidato per questo genotipo:** togliere la repressione … può
  > alzare l'output solo di un allele che produce un mRNA con 3′UTR … il cui problema è che la proteina
  > è instabile, non che l'mRNA sia scarso. **Più trascritto di una proteina destabilizzata è più
  > substrato di degradazione, non più funzione** (`PROTEIN_STATE_IDENTITY_GATE`).»*

⚠️ **The 2026-08 reasoning above is the general form of the argument, and it does not depend on NMD.**
It survives today's withdrawal intact, and it now applies to *both* alleles rather than one.

### 1.5 · Where the repo already names the boost tools

- `discovery_ledger_current.md:96` — `DL-MOL-004`, *"dCas9-VPR/CRISPRa sul promotore WWOX; small-molecule
  **WWOX-agonist** (toosendanin/TSN come tool, non clinico)"*, with the caveat, verbatim:
  *«⚠️ TSN è un tool di ricerca oncologico, non un farmaco pediatrico: serve solo a provare che WWOX
  è "drogabile" verso l'alto.»*
- `downstream_wwox_independent_rescue_census_20260921.md:79` — Toosendanin, PMID 34015398:
  *"hepatocellular carcinoma lines — ❌ **WWOX is being induced** … **NOT TRANSFERABLE** … **Category
  error for WOREE.** An agent that works by raising WWOX has nothing to raise in a null"*.
  🔴 **That verdict was written for a *null* genotype and does not transfer to a hypomorph** — which is
  precisely the genotype class this census is about. It is not a closure here.
- `working_model_current.md:231` / `disease_model.md:87` — *"Epigenetic option (future / ESPANSIONE):
  dCas9/CRISPRa upregulation of endogenous WWOX for **hypomorphic** states … **not actionable now**."*

### 1.6 · The one demethylation datum the repo already holds — and it is dead

`deepdive_manifests/PMID18460020.json:391` (Nakayama/Semba/Yokozaki 2008, *Cancer Sci*), verbatim locator:

> *"The supplementary figure S1 — **the sole evidence for the demethylation-restores-Wwox claim in the
> Discussion** — is hosted at blackwell-synergy.com, a domain retired when Blackwell merged into Wiley
> Online Library. The article's own pointer to its supplement is dead."*

And `fulltext_dossiers/PMID18460020.md:196` lists *"22% LOH · 20% promoter · 83% exon-1 methylation"*
under **"Four load-bearing results are 'data not shown'"**, annotated *"the entire epigenetic argument
of the Discussion"*.

🔴 **The only WWOX-demethylation claim LEGEND had already read in full text is supported by a figure
that cannot be retrieved and by prevalence numbers that were never shown.** That is not a positive row;
it is a warning about the class.

### 1.7 · The only CNS methylation record in the repo, and it is somatic

`fulltext_dossiers/PMID24510053.md:100` — *"**CNS content, all somatic:** WWOX LOH and promoter
methylation in **glioblastoma**, correlated with Bcl2 and Ki67"*. A tumour arising in the brain is not
a neuron, and a somatic epigenetic lesion in a glioma says nothing about a germline hypomorph.

---

## 2 · AGENT TABLE — everything reported to raise WWOX transcript or protein

Compiled from PubMed searches run 2026-09-22 (every `query_translation` inspected; all expanded
cleanly). **Every row's surrounding text was read** — the table relays no unread count.
Evidence class per the brief: `DIRECTLY MEASURED` / `INFERRED` / `AUTHOR INTERPRETATION` / `NOT PRESENT`.

### 2.1 · Class A — DNA-methyltransferase inhibitors (5-aza-2'-deoxycytidine / decitabine)

| # | Agent | System | Material | Species | Direction | Magnitude | Method | Transcript / protein | Evidence class |
|---|---|---|---|---|---|---|---|---|---|
| A1 | **Decitabine** (2.5–20 mg/m²/d, d1–5 ± d8–12) | Phase I trial, paired pre/post tumour biopsies, n=25 | **Human advanced solid tumours + lymphomas** (breast, kidney, H&N, lung, stomach, appendix, melanoma, thymic, NET, lymphoma, desmoplastic). **No CNS tumour. No normal tissue.** | human, in vivo | ↑ **in a minority** | pre-score ≤150 (n=17): median IHC **30 → 100**, **P = 0.0547** (not significant); **7 up / 8 unchanged / 2 down**; 3 of 6 initially-negative converted to positive | IHC score 0–300 (% cells × intensity), Abcam anti-WWOX 1:100 | **protein only** | `DIRECTLY MEASURED` (PMID **25024751**, PMC4094901, [DOI](https://doi.org/10.1186/1868-7083-6-13)) |
| A2 | **5-Aza-CdR** | HO-8910 ovarian carcinoma line + i.p. nude-mouse transplant | **human ovarian cancer line** | human / mouse host | ↑ | *"WWOX protein expression was **significantly higher** in the 5-Aza-CdR-treated group"* — **no numeric magnitude in the abstract** | MSP for methylation; protein by the paper's blot | **protein** (transcript not reported in abstract) | `DIRECTLY MEASURED` (PMID **24137423**, PMC3789030, [DOI](https://doi.org/10.3892/ol.2013.1438)) |
| A3 | **5-aza-2'-deoxycytidine (AZA)** | DU145 / LNCaP / PC-3 prostate lines | **human prostate cancer lines** | human | ↑ | *"most strikingly in DU145"* — no number | RT-PCR + Western | **transcript AND protein** | `DIRECTLY MEASURED` (PMID **16818616**, [DOI](https://doi.org/10.1158/0008-5472.CAN-06-0956)) |
| A4 | **5-aza-2'-deoxycytidine** | breast-cancer lines in vitro; **intratumoral injection** in nude mice | **human breast cancer lines** | human / mouse host | ↑ | not quantified in abstract; *"Alteration of global methylation levels was **not** observed"* | IHC/blot + xenograft growth | **protein** | `DIRECTLY MEASURED` (PMID **17200365**, [DOI](https://doi.org/10.1158/1078-0432.CCR-06-2038)) |
| A5 | **5-aza-2'-deoxycytidine (AZA)** | intrahepatic cholangiocarcinoma lines, in vitro **and** in vivo (xenograft) | **human ICC lines** | human / mouse host | ↑ | *"used to **activate the endogenous WWOX gene**"* — no magnitude in abstract | qRT-PCR, immunoblot, IF, IHC, MSP | **transcript + protein** | `DIRECTLY MEASURED` (PMID **25168293**, [DOI](https://doi.org/10.1111/jgh.12722)) |
| A6 | **5-aza-2'-deoxycytidine** | 9 pancreatic-cancer lines | **human pancreatic cancer lines** | human | ↑ | *"demonstrated **an increase** in the expression of WWOX"*; hypermethylation present in only **2/9** lines | MSP + real-time RT-PCR | **transcript** | `DIRECTLY MEASURED` (PMID **15073125**, [DOI](https://doi.org/10.1158/1078-0432.ccr-03-0096)) |
| A7 | **5-aza-dC ± TSA** | SNU-719 (EBV+) and SGC-7901 / BGC-823 / AGS gastric lines | **human gastric carcinoma lines** | human | ↑ (one of five genes assayed) | not separated per gene in abstract | MSP + qRT-PCR | **transcript** | `DIRECTLY MEASURED` (PMID **25720522**, [DOI](https://doi.org/10.1007/s12032-015-0525-y)) |
| A8 | **5-aza-dC + trichostatin A (combination)** | HSC-59 gastric line (hypermethylated) | **human gastric carcinoma line** | human | ↑ | *"**restored endogenous WWOX expression levels** in HSC-59 cells"* — no number | RT-PCR + Western | **transcript and/or protein** (abstract does not separate) | `DIRECTLY MEASURED` (PMID **20737170**, [DOI](https://doi.org/10.1007/s00428-010-0956-y)) |
| A9 | **AZA (± HDACi) protocol** | H1299 lung-cancer xenografts | **human lung cancer line in mouse** | human / mouse host | ↑ (asserted) | none given; the paper's **measured** arm is a *conditional transgene*, not the drug | xenograft growth; expression endpoint not specified in abstract | **not separable from abstract** | `AUTHOR INTERPRETATION` pending full text (PMID **17019711**, [DOI](https://doi.org/10.1002/ijc.22073)) |
| A10 | **Decitabine** | 1833 bone-metastasis xenograft | **human breast-cancer osteotropic clone in mouse** | human / mouse host | — (WWOX is context, not the measured target) | — | — | — | `INFERRED` / off-axis (PMIDs **28151481**, **28045433**) |

### 2.2 · Class B — HDAC inhibitors

| # | Agent | System | Material | Species | Direction | Magnitude | Method | Transcript / protein | Evidence class |
|---|---|---|---|---|---|---|---|---|---|
| B1 | **Sodium valproate** ⭐ | HO8910 ovarian line in vitro **and** nude-mouse xenograft | **human ovarian cancer line** | human / mouse host | ↑ | *"protein expression levels of WWOX and P27 were **elevated**"*; *"**up-regulated WWOX and P27 expression in nude mice**"* — **dose–response asserted for proliferation, not for WWOX; no magnitude, no n, no statistic given for the WWOX blot in the abstract** | Western blot **+ RT-PCR** | **transcript AND protein** | `DIRECTLY MEASURED` (PMID **23464470**, [DOI](https://doi.org/10.7314/apjcp.2012.13.12.6429)) |
| B2 | **Trichostatin A** (alone or + 5-aza-dC) | DU145/LNCaP/PC-3 (A3); HSC-59 (A8); gastric lines (A7) | **human cancer lines only** | human | ↑ | never isolated from the demethylating co-treatment in any abstract read | RT-PCR / Western / MSP | **transcript + protein** | `DIRECTLY MEASURED` **but confounded** — in A8 and A7 TSA is given *with* 5-aza-dC |
| B3 | **4-PBA** | — | — | — | — | — | — | — | `NOT PRESENT` for WWOX abundance. The repo carries it only as a *proteostasis* lead whose ER rationale is withdrawn (`DIS-004`, `N-11`) with an HDAC-inhibitor `REVIVAL_TRIGGER` that is about **HSP co-induction, not about raising WWOX** |
| B4 | vorinostat · romidepsin · entinostat · panobinostat · sodium butyrate | — | — | — | — | — | — | — | `NOT PRESENT`. PubMed returns **no WWOX record for any of them** (`query_translation` expanded all five correctly). 🔴 See §6 on tool trap (e) |

⭐ **B1 is the only agent in this entire census that is an approved CNS drug, crosses the blood–brain
barrier, and is already given to WWOX-DEE patients.** That is developed in §3.4 and §6 — it is the
single most consequential row here, and it is **one paper, in one cancer cell line, with no
replication anywhere** (PubMed: `valproate AND "WWOX"[Title/Abstract]` → **2 records**, of which one
is an unrelated 16q deletion case report).

### 2.3 · Class C — transcriptional / CRISPRa tools

| # | Agent | System | Material | Species | Direction | Magnitude | Method | Transcript / protein | Evidence class |
|---|---|---|---|---|---|---|---|---|---|
| C1 | **dCas9-VPR / CRISPRa on the WWOX promoter** | — | — | — | — | — | — | — | 🔴 **`NOT PRESENT` — `PREMISE: NOBODY_LOOKED`.** PubMed `WWOX AND (CRISPRa OR dCas9 OR VP64 OR "SAM system" OR CRISPR activation)` → **5 records**, every one eyeballed: one is a CRISPR **knockout** screen (34015398), the others are pre-CRISPR papers matching on the word *activation*. **No CRISPRa experiment has ever been published on this gene, in any system.** `TX-002` is a strategy name with zero published instance |
| C2 | **Ectopic WWOX** (Ad-WWOX, lentivirus, plasmid, AAV9-hSynI-hWWOX) | many | tumour lines, mouse brain, WOREE organoids | human/mouse | ↑↑ | large, dose-dependent, durable to P300 in the mouse (`DL-MOL-005`) | Western, IHC, phenotype | protein | `DIRECTLY MEASURED` — **but this is gene replacement, not an expression boost.** It is `TX-007`/`DL-MOL-005`, a different axis, and it is **genotype-agnostic by design**. Listed here only so it is not mistaken for evidence that *boosting* works |
| C3 | **Sp1 / Sp3** | 89 lymphoblastoid lines, pancreatic cancer cohort | human LCL + PDAC | human | rs11644322 **G** allele → more WWOX | EMSA + supershift + siRNA; exon 8→9 : core ratio ≈ 67 %, r = 0.68 | EMSA, qPCR | transcript | `DIRECTLY MEASURED` for the **polymorphism**; 🔴 `NOT PRESENT` for any **agent** — see §1.3 |
| C4 | **Kozak rs11545028** | 3 cell lines + oral-cancer cohort + GTEx | human | human | T allele **lowers** translation | luciferase p<0.05; IHC p=0.022 | luciferase, qPCR, IHC, eQTL | protein output | `DIRECTLY MEASURED` for the **polymorphism**; **no agent exists** that edits a Kozak context pharmacologically |
| C5 | **STAT3** | MCF-7 / MCF-7-HER2 + leptin ± tamoxifen | human breast lines | human | STAT3 binds the **WWOX promoter**; occupancy differs by line, with *"concomitant modifications of its mRNA/protein expression levels"* | ChIP + qPCR + Western | transcript + protein | `DIRECTLY MEASURED` (PMID **25539992**, [DOI](https://doi.org/10.1007/s13402-014-0213-5)) — but the direction here is **leptin/STAT3 suppressing pro-apoptotic WWOX**, i.e. an axis that would have to be *inhibited*, in a cancer context, with STAT3 controlling thousands of genes |
| C6 | **p53** | murine nervous system, p53-WT vs p53-KO | **mouse CNS** | mouse | **no effect** | *"expression profiles of WOX1 were found to be **similar in both p53 wild type and knockout mice**, suggesting that WOX1 expression is **not controlled by p53-mediated gene transcription**"* | IHC + Western | protein | `DIRECTLY MEASURED` **negative** (PMID **15026124**, [DOI](https://doi.org/10.1016/j.neuroscience.2003.12.036)). 🟢 A rare CNS-material row — and it closes a door |
| C7 | **UV-B** | primary human melanocytes | human melanocyte | human | 🔻 **WWOX consistently SUPPRESSED** by UVB across 6 independent lines | >2-fold class | Affymetrix U133 Plus 2.0 | transcript | `DIRECTLY MEASURED`, **wrong direction** (PMID **16888633**, [DOI](https://doi.org/10.1038/sj.jid.5700470)) |

### 2.4 · Class D — miRNA inhibition

| # | Agent | System | Material | Species | Direction | Magnitude | Method | Transcript / protein | Evidence class |
|---|---|---|---|---|---|---|---|---|---|
| D1 | **anti-miR-153 / antagomiR-153** | HCC lines in vitro; systemic antagomiR in a DEN mouse model | **liver** — hepatocellular carcinoma; **no brain arm** | human lines / mouse | ↑ WWOX protein, *"marcata"* | not quantified in the repo's record; the repo flags the source has substantive typos (*"miR-163"*, *"miR-300 mimics"*) → **trust-but-critical** | Western; 3′UTR luciferase; seed mutagenesis abolishes the effect | **protein** | `DIRECTLY MEASURED` in liver (PMID **25708809**, PMC4414157, [DOI](https://doi.org/10.18632/oncotarget.2927) — 🟢 **open access; LEGEND has never read it in full text**) — and the repo's own verdict is 🔴 **red, not promotable**, on pleiotropy (`HYP-20260709-03`) |
| D2 | **anti-miR-186-5p** | predicted 8mer site, 3′UTR pos. 637–644 (`ENST00000566780`), context++ −0.19 | bladder cancer | human | predicted ↑ | TargetScan prediction only; **never tested as an antagomiR on WWOX** | TargetScan | — | `INFERRED` — and already refused by `DL-MECH-069b` on the `PROTEIN_STATE_IDENTITY_GATE` |
| D3 | miR-134-5p · miR-214-3p · miR-153-3p · miR-24-3p · miR-187-5p · miR-670-5p · miR-625-3p · miR-29 family | Table 1 of the same source | assorted tumour contexts | — | — | — | — | — | `NOT PRESENT` as interventions. **Ten further miRNAs target the WWOX 3′UTR.** This is a *specificity* fact, not a lead: it means the 3′UTR is a busy, cell-type-specific regulatory hub, so any single antagomiR is one of eleven inputs |

### 2.5 · Class E — small molecules and physiological inducers

| # | Agent | System | Material | Species | Direction | Magnitude | Method | Transcript / protein | Evidence class |
|---|---|---|---|---|---|---|---|---|---|
| E1 | **Toosendanin (TSN)** | HCC lines + mouse metastasis model; found via a 19,050-gene CRISPR **knockout** screen | **hepatocellular carcinoma** | human lines / mouse | called a *"novel druggable WWOX **agonist**"* | 🔴 **no abundance number anywhere in the abstract.** The mechanism described is **re-wiring WWOX's protein–protein interactions** (Stat3, DVL2, GSK3β, by Co-IP), not raising its level | Co-IP, WB, in vivo metastasis | 🔴 **neither is demonstrated to rise.** *"Activation"* ≠ *"more protein"* | `AUTHOR INTERPRETATION` for the word **agonist** (PMID **34015398**, [DOI](https://doi.org/10.1016/j.canlet.2021.05.010)). Paywalled, no PMC. Toosendanin is a **triterpenoid neurotoxin** used as a botanical insecticide/anthelmintic |
| E2 | **Hyaluronidases (PH-20, Hyal-1, Hyal-2)** | murine developing nervous system | **mouse CNS — the only physiological inducer reported in neural material** | mouse | ↑ WOX1 | *"Hyaluronidases such as PH-20, Hyal-1 and Hyal-2 **induce the expression of WOX1**"* — stated as background, magnitude not given in this paper | IHC, Western | protein | `AUTHOR INTERPRETATION` in this paper (PMID **15026124**), with the primary elsewhere. 🔴 **Not a therapeutic object**: hyaluronidase signalling through HYAL-2–WWOX–SMAD4 is the **cell-death** pathway (§3.3) |
| E3 | **TGF-β1** | cell lines | tumour lines | human | dissociates the TPC6AΔ·WWOX complex | — | FRET, co-IP | — | `DIRECTLY MEASURED` for the complex, `NOT PRESENT` for WWOX abundance (PMID **25650666**) |
| E4 | resveratrol · curcumin · retinoic acid · statins · metformin · zinc | — | — | — | — | — | — | — | `NOT PRESENT` for WWOX abundance. The 21-record combined query was read end to end; no record reports one of these raising WWOX |

### 2.6 · Verified zeros, each labelled

| Query | Result | Label |
|---|---|---|
| CRISPRa / dCas9 / VP64 / SAM on WWOX | **no experiment exists** | 🔴 `PREMISE: NOBODY_LOOKED` |
| Any agent tested on WWOX abundance in **a neuron, brain, iPSC-neuron, organoid or non-malignant human cell** | **none** | 🔴 `PREMISE: NOBODY_LOOKED` |
| `WWOX AND (5-aza-dC OR decitabine) AND (neuron OR brain OR fibroblast OR lymphoblastoid OR non-cancer)` | **1 record**, and it is the cholangiocarcinoma paper (A5) whose *"in vivo"* is a xenograft | 🔴 verified zero |
| Any agent that raises WWOX in **a WWOX-DEE / SCAR12 genotype**, of any allele class | **none** | 🔴 `PREMISE: NOBODY_LOOKED` |
| Any measurement of WWOX **solubility, aggregation or folding state after a boost** | **none.** The 18-record solubility/aggregation set and the 12-record agent set are **disjoint — zero papers in both** | 🔴 `PREMISE: NOBODY_LOOKED` |
| vorinostat · romidepsin · entinostat · panobinostat · butyrate on WWOX | **no records** | 🟡 zero, but see §6 on trap (e) |

**A verified zero is a finding. None of the above is evidence of absence.**

---

## 3 · SAFETY — the half that decides the axis

### 3.1 · Tumour-suppressor risk — what the repo actually measured

Three records, and they do **not** all say the same thing:

- `fulltext_dossiers/PMID17575124.md:9` — *"This is a **carcinogen-susceptibility experiment**, not
  evidence that heterozygotes spontaneously phenocopy WWOX developmental disease. After six NMBA doses,
  **25/26 heterozygotes versus 10/34 wild types** developed forestomach tumors; **7/26 heterozygotes and
  0/34 controls** had invasive SCC."*
- `fulltext_dossiers/PMID17360458.md:9` — *"In adult heterozygotes, spontaneous tumor-bearing animals
  were **10/58 versus 2/60** WT; after **ENU**, tumor incidence was **37/46 versus 20/42**."*
- `discovery_ledger_current.md:1042` — Aldaz 2014 (PMID 24932569, full text), verbatim:
  *"loss of one Wwox allele (i.e. **haploinsufficiency**) appears **not to be deleterious or
  carcinogenic** in the longer-lived heterozygous mice"*; *"The lifespan of the Wwox heterozygotes was
  **indistinguishable from WT mice**."*

🟢 **Direction of the risk, stated plainly: the tumour-suppressor hazard in WWOX runs with LOSS, not
with gain. Every one of these experiments is a *too-little* experiment.** The repository holds **no**
experiment in which WWOX was raised above wild-type and tumours followed. **The oncological direction
of a boost is, as far as anything measured goes, safe** — which the ledger already says
(`HYP-20260709-02`: *"In tutti e tre, ↓WWOX = peggio → la direzione «aumentare WWOX» è oncologicamente
sicura"*).

⚠️ **But the agents are not.** The tumour-suppressor risk here attaches to the **modality**, not to
WWOX: decitabine and azacitidine are cytotoxic nucleoside analogues that hypomethylate the genome
globally, and in A1 the required dose caused enough myelosuppression that **filgrastim had to be added
at higher dose levels**. Global hypomethylation de-represses oncogenes and retroelements alongside
tumour suppressors. **Giving a genotoxic hypomethylating agent, chronically, to a child, to raise a
tumour suppressor by a non-significant margin, is a risk profile no reading of this census supports.**

### 3.2 · The proteotoxic flag — now on both alleles

`HYP-20260709-02` carries it verbatim:
> *«🟡 **giallo.** Non per tossicità d'organo, ma per **rischio proteotossico** … Più sintesi di una
> proteina destabilizzata (ΔΔG +1.51 kcal/mol) in un neurone può essere neutro **o dannoso**. …
> **L'obiettivo è ripristinare la funzione fisiologica, non sovra-attivare.**»*

The withdrawal **widens** this flag rather than relieving it: `CC-20260922-NMD-PREMISE-WITHDRAWAL-01` §3
states *"🟡 **The proteotoxic safety flag stands — and now applies to both alleles, not one.**"* Under
the surviving outcome the acceptor allele makes `p.Gln353_Gln354del`, a **packing/stability lesion**
removing both partners of a six-contact polar staple including the helix's own N-cap. **A boost would
therefore raise the output of two structurally compromised proteins, not one.**

🔴 **And nobody has ever measured WWOX protein *quality* after any boost, in any system.** §2.6 records
the disjoint-set result. Every one of the twelve agent papers reports **abundance** — IHC score, band
intensity, qPCR — and not one reports solubility, detergent fractionation, aggregation, localisation,
turnover or function. This is exactly the failure the repository already named:
`PROTEIN_STATE_IDENTITY_GATE` — *"abundance ≠ function; 'stable but inert' is a demonstrated phenotype"*
(`framework/eval/failure_taxonomy.md:15`).

### 3.3 · Neuronal tolerability — and a signal that runs the wrong way

🔴 **The only neural material in which WWOX is documented to RISE is injured neural material, and the
rise accompanies death.**

- PMID **15664696** ([DOI](https://doi.org/10.1016/j.neuroscience.2004.07.054)) — rat/mouse retina:
  *"In the damaged inner and outer nuclear layers of rat retina, **WOX1 and p-WOX1 were overly
  expressed**"*; *"In rd mice with an inherited retinal deficiency, **upregulation of WOX1 and p-WOX1
  in degenerated retina was observed with age**"*; conclusion: *"**activated WOX1 is likely to exert
  apoptosis of neuronal cells**."*
- PMID **27999774** ([DOI](https://doi.org/10.3389/fcell.2016.00141)) — *"When rats are subjected to
  **traumatic brain injury**, over accumulation of a HYAL-2–WWOX complex occurs in the nucleus to
  **cause neuronal death**."*
- PMID **27845895** ([DOI](https://doi.org/10.18632/oncotarget.13268)) — *"the Hyal-2/WWOX complex was
  accumulated in the apoptotic nuclei of neurons in the rat brains in 24 hr post injury"*; and
  *"causes **bubbling cell death** when the signaling complex is **overexpressed**."*
- The repo's own line, `HYP-20260709-02`: *"WWOX è pro-apoptotico in contesti sperimentali (Drosophila:
  WWOX↑ → ROS↑, potenzia l'eliminazione cellulare Egr/TNFα-mediata)"*; and `N-05`: *"**Neither too
  little nor too much WWOX.**"*

⚠️ **The honest reading of these, stated with its limits.** They do **not** show that raising WWOX kills
neurons — the rises are *correlates of* injury, the direction of causation is not established in any of
them, and the *"bubbling cell death"* result is on an **overexpressed ectopic complex**, which is a
different object from a modest endogenous boost. **But they are the only neuronal WWOX-abundance
literature that exists, and all of it points the same way.** An axis whose entire neural evidence base
consists of "WWOX goes up when neurons die" cannot be advanced on a presumption that up is good.

🟢 **The counterweight, which must be stated with equal force:** gene replacement raises neuronal WWOX
far above any boost and **rescues** the mouse (`DL-MOL-005`: dose-dependent, durable to P300, neuron-specific
hSynI promoter, survival + seizures + myelination + gliosis + glucose + ataxia). So high neuronal WWOX
is demonstrably **not** intrinsically toxic in a null background. 🔴 **The two bodies of evidence are
not reconciled by anyone**, and the variable that would reconcile them — *whose* WWOX, wild-type or
destabilised — is precisely the one nobody has measured. **`DL-MECH-009` also records the opposite
design worry for AAV (the WPRE overexpression tension), so "too much" is a live concern inside the
replacement arm too.**

### 3.4 · CNS penetration, by class

| Class | CNS penetration | Evidence grade |
|---|---|---|
| **Decitabine / azacitidine** | Not established for this purpose. PubMed `(decitabine OR azacitidine) AND (blood-brain barrier OR CSF OR brain penetration)` returns **21 records**, and the standard pharmacology of a hydrophilic nucleoside analogue is poor CNS exposure — but 🔴 **`PREMISE: DEFAULT_FROM_TEXTBOOK`: I did not read those 21 records and I am not asserting a value.** What I can assert is that **no record anywhere pairs a demethylating agent with WWOX in brain tissue** | unread |
| **Valproate** | 🟢 **Excellent — and this is the only class where CNS delivery is a solved problem.** It is a standard antiseizure medication in this very disease | established by clinical use, not by a WWOX experiment |
| **Toosendanin** | Unknown for this purpose; it is a **neurotoxin** (presynaptic blocker) in its own right — a property that argues against, not for | not assessed |
| **antagomiRs** | Unsolved for the immature CNS. The repo's verdict (`HYP-20260709-03`) is 🔴 red | — |
| **CRISPRa** | `DL-MOL-004` verbatim: *"delivery CRISPRa al SNC immaturo **non risolto**"* | — |

---

## 4 · SPECIFICITY — is anything here WWOX-selective?

Applying the `PAPER 050` standard from §1.3 (**wrong direction** ∨ **thousands of genes** ⇒ dead):

| Agent / class | Genes affected | WWOX-selective? | Verdict under the Sp1 standard |
|---|---|---|---|
| Decitabine / 5-aza-dC | the **entire methylome**; A1's own control gene set (FHIT, FUS1, PTEN) moved in the same patients, and A4 measured *"Alteration of global methylation levels was not observed"* while A1 used **LINE-1 global methylation** as its surrogate | 🔴 **No — maximal shotgun** | **Fails.** And note A1 found WWOX change did **not** correlate with LINE-1 demethylation (Spearman r = **−0.04**, P = **0.87**, n = 19) — so even the *mechanism* is not demonstrated |
| HDAC inhibitors (valproate, TSA) | thousands, plus valproate's own non-HDAC pharmacology | 🔴 **No** | **Fails on specificity.** Direction is right; selectivity is absent |
| Sp1 modulators | *"Sp1 controlla migliaia di geni"* and *"quasi tutti … lo inibiscono"* | 🔴 **No** | **Already failed — twice over.** This is the repo's own precedent |
| STAT3 modulation | thousands; and the reported direction is WWOX **suppression** by leptin/STAT3 | 🔴 **No** | **Fails on both criteria** |
| antagomiR-153 / -186-5p | miR-153 has documented targets incl. **PTEN and AKT**; the WWOX 3′UTR has **eleven** reported miRNA inputs | 🔴 **No** | **Fails.** Already 🔴 red in the ledger |
| Toosendanin | screened out of a 19,050-gene knockout library; a triterpenoid neurotoxin | 🔴 **No**, and 🔴 **direction not even demonstrated** | **Fails on evidence class before specificity is reached** |
| **dCas9-CRISPRa on the WWOX promoter** | in principle **locus-selective — the only entry in this table that is** | 🟢 **Yes, by design** | 🔴 **But it has never been built for this gene, and CNS delivery is unsolved.** Selectivity is a property of a tool that does not exist |

🔴 **The result is categorical: every agent for which a direction has been measured is a shotgun, and
the only WWOX-selective modality has never been applied to WWOX.** That is the same shape as the Sp1
rejection, repeated across six independent agent classes.

---

## 5 · VERDICT — is there a credible boost lead?

# 🔴 NO.

Not one agent clears the repository's own three-part standard for a lead — *a measured direction, a
tolerable specificity profile, and a readout tying abundance to function.* Stated per criterion:

| Criterion | Status |
|---|---|
| **Measured direction** | ✅ met by ten agents — **all in tumour material, none in a neuron, none in a WWOX-DEE genotype, none in a non-malignant cell** |
| **Tolerable specificity** | 🔴 **failed by every agent with a measured direction.** The only selective modality (CRISPRa) has no published instance on this gene and no CNS delivery |
| **Abundance tied to function** | 🔴 **failed universally.** Zero papers measure WWOX solubility, aggregation, localisation or function after any boost. `PROTEIN_STATE_IDENTITY_GATE` is unsatisfied everywhere |

**What is missing, named exactly:**

1. **A substrate.** Every demethylating-agent result works by reversing a **somatically acquired
   promoter hypermethylation of a cancer cell**. 🔴 **Nobody has shown the WWOX promoter is methylated
   in a WWOX-DEE neuron — or in any non-malignant neural tissue.** If it is not, the agent has nothing
   to demethylate and the whole of Class A is a category error for this disease. **This is the single
   biggest unmeasured premise in the census, and it is upstream of everything in §2.1.**
2. **A material.** The entire positive table is oncology. Per the brief's own bound, it does not
   transfer.
3. **A functional readout.** Abundance is all anyone has measured.
4. **A direction in a neuron.** The only neuronal WWOX-abundance literature associates *rises* with
   injury and death (§3.3).

**What the withdrawal did and did not change.** It removed one wrong argument — the NMD asymmetry —
and it was right to remove it. It **did not** supply a lead. The axis moves from *"closed for a reason
that turned out to be false"* to *"open, unsurveyed, and — now surveyed — empty of credible agents."*
🟢 That is a better epistemic state than before, and it is still a negative.

**What survives as principle, not as molecule.** Three things are established and worth keeping:
(a) WWOX transcription and translation **are** genuinely modulable bottlenecks (Kozak, Sp1, miR-153,
demethylation) — the locus is not refractory; (b) raising WWOX is **oncologically safe in direction**
(§3.1); (c) `DIS-003` now covers only one of the two alleles. None of those three is a lead. All three
are reasons the axis should stay **open and parked** rather than closed again.

⛔ **Nothing here is a recommendation. No agent named in this document should be given to anyone on the
basis of anything in it, and valproate's use in this disease is a decision for a treating clinical team
on antiseizure grounds that have nothing to do with WWOX abundance.**

---

## 6 · WHAT I COULD NOT ESTABLISH — and the cheapest thing that would move it

### 6.1 · Reported as prominently as the positives

| # | Could not establish | Why | Cost to fix |
|---|---|---|---|
| U1 | 🔴 **Whether the WWOX promoter is methylated at all in a WWOX-DEE / hypomorph neuron** | never measured by anyone; every methylation datum is from a tumour | **zero** if public brain methylomes are queried; §6.2 |
| U2 | 🔴 **Whether any boost changes WWOX protein *quality*** | the agent set and the solubility/aggregation set are **disjoint** | one fractionation blot on an existing boost experiment |
| U3 | **The magnitude of every Class A and B effect** | eight of ten abstracts give a direction and no number; only A1's full text was retrieved, and it gives medians and a **non-significant** P | full texts of A2, A3, A5, B1 |
| U4 | 🔴 **Whether B1 (valproate → WWOX) is real** | one paper, *APJCP* 2012, **no PMC, no open access, never replicated**; `get_copyright_status` returns `source: "not_available"`. Same cell line (HO8910/HO-8910) and same city as A2 — **the two are probably not independent** | one ILL request; or one blot |
| U5 | **Whether A9 measured WWOX abundance at all** | its measured arm is a conditional transgene; the drug arm's expression endpoint is not in the abstract | one full text |
| U6 | **Whether the acceptor allele's predicted 412-aa product responds to a boost** | 🔴 the product has never been observed. `TX-001`'s RT-PCR has never been run | the §7 experiment of the withdrawal CC |
| U7 | **Reagent-level completeness of the agent census** | 🔴 **Tool trap (e) applies to this entire document.** An agent named only in Methods is invisible to `[All Fields]`. My B4 and E4 zeros are therefore **weaker than my A- and B1-row positives**. The positives were found because the agent is in the *title or abstract*; anything used incidentally in a Methods section is missed at an unknown rate, measured at **100 % for cycloheximide in this gene** | full-text sweep, not a query |

**Blocked routes, recorded once and not retried** (§27; a tool block is not a scientific stop): general
web egress 403s at CONNECT, so publisher landing pages, GTEx/Ensembl and any non-PubMed database were
unreachable in this act. Everything above is from PubMed and the committed tree.

### 6.2 · The cheapest record that would move the verdict — in order

1. 🥇 **U1, and it costs nothing but a query.** *Is the WWOX promoter methylated in normal human brain?*
   Public reference methylomes (Roadmap / ENCODE / BLUEPRINT brain, and any WWOX-DEE fibroblast or LCL
   array) answer it without a wet experiment. **If the WWOX promoter is unmethylated in neural tissue —
   which is the expectation, since WWOX is *"generally strongly expressed in various normal tissues"*
   (PMID 25024751 full text, Background) — then the entirety of Class A is closed for this disease by a
   single fact, and the census's largest branch is settled for free.** Nothing else in this document
   has that leverage-to-cost ratio. *(Egress was blocked today; this is a route, not a result.)*
2. 🥈 **U4, one interlibrary-loan request.** The valproate row is the only agent in the census that is
   CNS-penetrant, approved, paediatric and already in use in this disease. It rests on **one
   unreplicated paper in a journal with no PMC deposit**. Read it, or discount it. Either outcome is
   worth more than any new search.
3. 🥉 **The natural experiment that is already running, and nobody has sampled it.**
   🔴 **WWOX-DEE patients are given valproate.** The repository records it repeatedly —
   `wwox_neonatal_parkinsonism_audit_20260921.md:53` (*"seizure-free for 1 month on valproic acid and
   clobazam"*), `:107` (*"After valproic acid was introduced, the frequency of spasms decreased"*),
   `deepdive_manifests/PMID39507621.json:168` (*"phenobarbital, valproic acid, carbamazepine… No
   sustained positive effect"*), `paper_registry_current.md:6447` (*"risposta parziale a valproato +
   lamotrigina"*). **If B1 is real, then some WWOX-DEE patients have been receiving a WWOX-raising HDAC
   inhibitor for years — and WWOX has never been measured in any of them, on or off drug.** The cheapest
   design that exploits this is **not a trial**: it is a ±valproate WWOX Western on **carrier-derived
   LCLs**, which cost nothing to obtain and supply the internal control every existing WWOX measurement
   lacks. ⚠️ **This is an observation about an unmeasured variable, not a suggestion to start, stop or
   change anyone's medication.**
4. **The experiment, if one is run at all.** Not a boost experiment. **The `TX-001` junction RT-PCR**
   (`CC-20260922-NMD-PREMISE-WITHDRAWAL-01` §7, with its four constraints) — because until the acceptor
   allele's product is observed, *"boost both alleles"* has one known object and one imagined one. And
   per the withdrawal's own standing rule: **no re-score until mechanism + reagent + allele verification.**
   Every agent in §2 stays unscored until then.
5. 🟢 **One free full text that LEGEND does not hold.** The miR-153 primary (D1) is **PMID 25708809 /
   PMC4414157 / [DOI](https://doi.org/10.18632/oncotarget.2927), open access** — and the repository's
   entire record of it is second-hand prose in `HYP-20260709-03`, including the caveat that *"la
   sequenza/posizione del sito 3'UTR è **solo in figura**, non nel testo"* and that the paper carries
   substantive typos. **It is the only experiment in this census in which inhibiting a repressor raised
   WWOX protein in a living animal**, and nobody here has read it. Reading it costs one call and would
   convert D1's magnitude from `not quantified` to a number — or expose the row as unsupportable. It
   does not make the agent a lead (it is 🔴 red on pleiotropy either way); it settles whether the
   *principle* is as well demonstrated as the ledger claims.
6. **The readout that must be built into whatever comes first.** Any future boost experiment on this
   genotype must carry a **soluble/insoluble fractionation and a function assay alongside the abundance
   blot**, pre-specified. Without it the experiment reproduces the census's universal defect and cannot
   answer the question that reopened the axis.

---

## 7 · Standing flags for the orchestrator

- ⛔ **Nothing above is scored, ranked or promoted.** FLAG FIRST holds.
- 🔴 `DIS-003` should be **narrowed, not revived** — its premise is Q230P-homozygous fibroblasts and it
  says nothing about the acceptor allele. Its own `REVIVAL_TRIGGER` (compound-heterozygous transcript)
  is now arguably live. **Proposed, not applied.**
- 🔴 `N-05`'s allele-asymmetry half inherits the withdrawn NMD premise and should be marked accordingly.
  **Proposed, not applied.**
- 🟡 `downstream_wwox_independent_rescue_census_20260921.md:79`'s toosendanin verdict (*"nothing to raise
  in a null"*) is correct **for a null** and does not transfer to a hypomorph; but E1 fails on evidence
  class anyway, so the axis does not open there.
- 🟢 The oncological-safety direction in `HYP-20260709-02` is **corroborated** by this census (§3.1) and
  needs no change.
- 🔴 The proteotoxic flag should be carried onto **both** alleles, per the withdrawal CC §3.

---

*End of census. Scientist R, 2026-09-22. No canonical file was edited; no BATCH_COMMIT was run.*
*Not medical advice.*
