# What could be done for a WWOX-DEE patient WITHOUT restoring WWOX — a node map, a selectivity audit, and an outcome-width score

**Node:** `DOWNSTREAM_NODE_MAP_AND_TRACTABILITY` · **Actor:** Scientist F · **Date:** 2026-09-22

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, every registry,
> every queue, every ledger, every receipt and the state manifest. **Nothing here was promoted, nothing
> committed, no `BATCH_COMMIT` run, no receipt claimed, no git command executed.**
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is described.
>
> 🔴 **Nothing here is medical advice.** 🔴 **BLOCK-1 applies throughout.** Every compound named below is a
> **mechanistic hypothesis**, not a treatment. **No dose, no route, no schedule, no clinical framing, and no
> suggestion that anything be given to anyone appears anywhere in this file.** Any clinical question is
> `HUMAN_REQUIRED` and belongs to a treating team.
>
> 🔴 **Alleles and models are never pooled.** `Wwox`-null (and the two independent targeting strains within
> it), `gt/gt` hypomorph, `P47T` knock-in, Synapsin-Cre `S-KO`, Nestin-Cre `N-KO`, rat `lde/lde`, human WOREE
> and human SCAR12 are different objects. **The `gt/gt` hypomorph has no published brain WWOX quantification
> and no neurological phenotyping — that is a missing measurement, never evidence of absent brain protein**,
> and it is why `gt/gt` appears in no row of §1.

---

## 0 · Read depth, and how the baseline was enumerated

**Enumeration method, declared because four actors failed it today by reading only the file that looked
canonical.** I **listed first, then grepped across everything listed** — `find` over `disease-models/wwox/`
(137 files in `analysis/` alone, plus `registries/`, `research/`, `therapeutics/`, `meta/`), then
case-insensitive `grep` for each candidate node's vocabulary across the whole tree plus `framework/`,
`learning/`, `reviews/` and `governance/`. The GSK3β/lithium check demanded by the brief was run **first**
and returned **prior adjudication in at least eight separate places** (§0.2). Nothing in this file re-derives
it.

| Surface | Depth in this act |
|---|---|
| `downstream_wwox_independent_rescue_census_20260921.md` (Scientist B, 743 lines, Waves 1–2) | 🟢 **read in full** |
| `mechanism_intervention_map.md` (951 lines, M1–M10 · R-01…R-09 · N-01…N-15 · E-1…E-10) | 🟢 **read in full** |
| `superior_node_search_20260922.md` (Scientist F, earlier slot today) | 🟢 **read in full** |
| `claim_registry_current.md` — CLAIMs 003, 004, 005, 006, 016, 021, 029, 031, 035, 036, 037, 038, 039 | 🟢 read at block level |
| `working_model_current.md` · `therapeutic_strategies_current.md` (TX-001…TX-007) · `therapeutic_hypotheses_ledger_current.md` (HYP index) | 🟢 read |
| `postdiagnosis_window_evidence_20260922.md` (Scientist G, today) · `denominator_audit_therapeutic_portfolio_20260922.md` (Scientist B, today) · `wwox_myelin_oligodendrocyte_census_20260921.md` · `wwox_engagement_partner_adjudication_20260922.md` | 🟢 read at the sections bearing on this node |
| `discovery_ledger_current.md` — DL-MOL-010, DL-MECH-036 and the entries cited by the files above | 🟡 targeted sections |
| **External fetches (PubMed/PMC) in this act** | 🔴 **NONE.** This file is an **analysis over material already held**. It therefore makes **no new absence claim from a search** and **no figure-panel claim** — every panel value below travels with the receipt of the session that inspected it. |

🔴 **Consequence, stated up front so no reader over-weights this file.** Because no surface was fetched here,
**every quantitative datum below is a prior-session attestation**, and every "nobody has measured X" is
**quoted from a prior LEGEND measurement of that absence**, never asserted by me. A PubMed count of zero is
not evidence; none of the zeros in this file is mine.

### 0.1 · What this file adds, and what it deliberately does not repeat

Two artefacts already occupy adjacent ground and **must not be re-derived**:

| Prior artefact | What it enumerated | What it did **not** do |
|---|---|---|
| `downstream_wwox_independent_rescue_census_20260921.md` | **INTERVENTIONS** — 12 rows; exactly **4 positive arms in the entire literature**, none rescuing a disease endpoint | It is keyed to drugs, not to **nodes**; it does not classify anything as upstream/downstream of the seizures; it does not score outcome width |
| `superior_node_search_20260922.md` | A search for a node **superior to the portfolio**; found none; produced one deepening (Tau's microtubule polymer), two flags, one kill, one contested sign | It is a ranked *search*, not a *map*; it audits no intervention's selectivity; its verdict filters are window/endpoint/arm, not selectivity/width |

**This file's three additions, and they are the only things in it that are new:**
1. a **node-keyed map** carrying, for each node, the column neither prior file has — **is this node upstream or downstream of the seizures**, which decides whether treating it could matter at all (§1);
2. a **selectivity audit run as a gate**, in which an intervention whose off-target profile is unrecorded is **demoted to a question**, regardless of how good its node is (§2);
3. an **outcome-width score**, which re-ranks the nodes and puts the *best-evidenced* node **out** of the top three, on the session's own rule (§3, §4).

### 0.2 · 🔴 GSK3β and lithium — prior adjudication, located before writing, reproduced as a pointer only

The brief required this check. It returns, in **eight** places:

| Where | What it already holds |
|---|---|
| `CLAIM 016` evidence boundary (propagated `BATCH_20260810_005`) | Lithium's PTZ suppression is significant in **all three genotypes, wild type included** ⇒ *"l'esperimento non stabilisce un rescue farmacologico WWOX-specifico"* |
| `CLAIM 035` | WWOX is a **direct, residue-mapped** inhibitor of GSK3β via an Axin-like motif 388–407, **L404 strictly required**, **S9-independent** ⇒ de-repression is **invisible to a phospho-S9 western** |
| `mechanism_intervention_map.md` §4 R-04 | Lithium scored **T5, not T2** — "an anticonvulsant working in a model that has seizures" |
| `mechanism_intervention_map.md` §5 N-02 | `REVIVAL_TRIGGER` recorded: a PTZ arm with an explicit **tested** `−/−` vs `+/+` contrast, or a different GSK3β inhibitor under the same design |
| `DL-MOL-003` | Lithium is **directionally contra-indicated** on the Wnt axis — it stabilises β-catenin, which is already hyperactivated |
| `DIS-009` | The "a WWOX-mimetic is safer than lithium because WWOX is substrate-selective" argument is **rejected** — the same paper's Supplementary Figure shows generic docking-site block on an unrelated substrate |
| `CC-20260826-GSK3B-S9-AXIS-01` · `CC-20260826-LITHIUM-BOUNDARY-01` | The commit candidates that carry both |
| `PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION_{LETTORE,SCIB}_v1` | Two independent scientist adjudications of the same figure |

⇒ **Lithium is settled and is not reopened here.** GSK3β appears in §1 as a **node**, with its seizure link
carried at the status the repository gives it, not at the status a drug result was once read as giving it.

---

## 1 · THE NODE MAP

**Admission rule.** A row is admitted only if the consequence is `DATO` or **strong** `INFERENZA` in *this*
repository, **and** an intervention on it would not require WWOX to be present. Rows that fail the second
test (WWOX restitution, CRISPRa, WWOX-mimetics, toosendanin) are **out of scope by construction** and are not
listed — the census already classified them.

🔴 **The column that decides everything is `Relation to the seizures`.** Under `CLAIM 031` / `N-15`, cognitive
and psychomotor impairment **precedes** the epileptic encephalopathy and **does not improve** when epileptic
activity is controlled. So a node that lies **downstream of the seizures** can, at best, be corrected without
changing development; a node **parallel to** or **upstream of** them is the only place a downstream lever
could in principle buy anything developmental.

| # | Node | Evidence class · source · **model/allele (never pooled)** | Relation to the seizures | Does an intervention exist at all? | 🔴 SELECTIVE for the node, or merely ADJACENT? |
|---|---|---|---|---|---|
| **A** | **GSK3β de-repression** — loss of a *physical* brake at the Axin-like docking site 388–407, L404 required, S9-independent | `DATO`, residue-resolved, 5 orthogonal assays — `CLAIM 035` (PMID 22193544, biochemistry + SH-SY5Y + **endogenous mouse-brain co-IP**). Abundance elevated in cortex/hippocampus/cerebellum — `CLAIM 016`, **NCKU `Wwox`-null mouse** | 🔴 **UNRESOLVED, and the repository says so.** The GSK3β-state → seizure-susceptibility link *"rests entirely on one non-selective drug, with no molecular confirmation that the drug engaged the target in these animals, no second inhibitor, no genetic test, and no interaction test"* (`PHASE1_PMID32000863_SCIC_FIRSTPASS_v1`). Epistemic type there: `IPOTESI` | Yes — (a) lithium (settled, §0.2); (b) an **Axin-site ligand**, which does not exist | 🟡 **ADJACENT at best today.** `H-1` proposes *isoform* selectivity (Axin associates more readily with β1; tau is a **disfavoured** substrate for β2; an ATP-competitive inhibitor **cannot** separate the isoforms, an Axin-site ligand could) — `DL-MECH-067`, `DL-MECH-068`. 🔴 **That Axin-site binding confers β1 preference has never been measured on WWOX.** `PREMISE: INFERENZA` |
| **B** | **Tau's microtubule-binding competence — the polymer, one layer below the kinase** | `DATO` ×6 / `INFERENZA` ×1 / `IPOTESI` ×1 — chain L1–L8 in `superior_node_search_20260922.md` §3 NODE 1, built on PMID 22193544 read in full earlier today; MAP2 reduced at every age with neuron number, cortical thickness and laminar distribution **intact** in the **rat `lde/lde`** (`DL-MECH-027`, PMID 31340538) | **PARALLEL.** Dendritic/axonal arborisation, not excitability. Nothing links it to a seizure in any WWOX model | 🔴 **No.** Nothing in the portfolio acts at the polymer; **no arm exists in any WWOX system, ever** | 🔴 **The selectivity question inverts here, and this is the most important cell in the table.** The modality the tauopathy field would import — **Tau-lowering** — is highly selective *and is predicted by the primary data to be HARMFUL*: *"Neither WWOX overexpression nor GSK3 knockdown promoted neurite outgrowth in the Tau knockdown condition, indicating that Tau is the effector of both WWOX and GSK3."* **Tau is the effector of the benefit, not the toxin.** A microtubule-stabilising direction is the mechanistically coherent one and **no such agent has been evaluated here** |
| **C** | **Neocortical E/I imbalance — spontaneous bursting, altered oscillatory organisation, ↑phase–amplitude coupling; bursting DEPENDS on NMDAR activity** | `DATO` — `CLAIM 021`, **Synapsin-Cre neuron-specific `Wwox` S-KO mouse**, neocortical slice P13–P17. The dependence was established **pharmacologically**: d-APV **eliminated** the spontaneous bursting, reversibly on washout (receipt `FTR-20260810-34634460-02`; `E-1` discharged ⇒ **T1 for the tool compound**) | 🔴 **This node IS the seizure mechanism**, not something upstream of it. Under `N-15` that caps what correcting it can buy | Yes — **memantine** (approved elsewhere) as the translational object; d-APV / MK-801 as tools. 🔴 **Memantine has never been given to a WWOX system** | 🟡 **UNKNOWN in this repository.** d-APV is a competitive NMDAR-site tool, not a therapeutic object. **For memantine this repository records no off-target profile and no potency ratio of any kind** (§2). And the authors' own bound travels with the arm: recordings at **P13–P17** in animals dying at 3–4 weeks *"may mimic a late-stage disorder"* |
| **D** | **Gap-junction / pannexin contribution to the same bursting** | `DATO` that an arm exists; **non-attributable** — same S-KO slice. CBX reduced burst frequency ~87%, *"This did not return to normal levels after washout"*; the **selective** pannexin-1 blocker BB-FCF **went the wrong way** (normalised burst frequency ≈2.55 vs baseline 1.0, no test drawn) — LEGEND's `N-16` | Same as C — it is the seizure mechanism | Tools only | 🔴 **FAILS, and it is the cleanest worked example in the file.** CBX blocks **NMDAR and pannexin**, and an effect surviving washout is not cleanly pharmacological. The one **selective** agent in the pair produced a **negative in the wrong direction**. ⇒ The node's apparent strength came entirely from the **non-selective** reagent |
| **E** | **Hypomyelination via non-cell-autonomous OPC maturation failure** | `DATO` — `CLAIM 003`/`CLAIM 004`, **Synapsin-Cre S-KO and Nestin-Cre N-KO reproduce it; Olig2-Cre and GFAP-Cre produce no evident anomaly**; oligodendrocytes are **never transduced** by the rescuing vector and myelin improves anyway. Human limb: serial MRI *"delayed myelination"* from **day 19 of life**, progression in 7/13 (`postdiagnosis_window_evidence_20260922.md`) | **PARALLEL / DOWNSTREAM OF THE NEURON.** Not shown to cause the seizures in any model | Yes — pro-myelinating agents as a class | 🟡 **ADJACENT by construction.** `N-13` deprioritises the class on **compartment**: the OPCs are present and *"not receiving the axonal signal"*, so pushing them alone yields little. 🔴 **Not `refuted`** — the oligodendrocyte-directed AAV arm is **confounded by the authors' own admission** (*"may reflect the limited oligodendrocyte tropism of AAV9 … rather than a lack of relevance"*), and the neuron-only rescue is **incomplete**, the residual gap attributed by the authors — as **their `IPOTESI`** — to an oligodendrocyte-autonomous WWOX function |
| **F** | **Astrogliosis / microglial activation** | `DATO` at **area-fraction** level — `CLAIM 005`, **systemic constitutive `Wwox`-KO (BK5-Cre), two weeks**: IBA1/GFAP area fraction up in CA1, CA3, whole hippocampus; only `Il6`, **not** `Tnf-a`, significant. Progressive astro-microgliosis in the **`P47T` knock-in**, a different allele — `CLAIM 006` | 🔴 **DOWNSTREAM — of the neuron, and plausibly of the seizures.** Neuron-restricted WWOX rescue **by itself** reduces gliosis (`CLAIM 004`) ⇒ part of this axis is a **consequence** | Class-level only — **no compound is identifiable in the public record** (`R-06`) | 🔴 **CANNOT BE AUDITED AT ALL.** An intervention with no named molecule has no selectivity profile to state. Under the §2 gate it is not a candidate and not even a question — it is a **class label** |
| **G1** | **Neuronal bioenergetics — HIF1α de-repressed in normoxia → PDK1 ↑ → pyruvate blocked at TCA entry** | `INFERENZA`, and the repository grades it **weak**: PDK1/GLUT1/HK2/PKM2 measured up in **`Wwox`-KO MEFs**; OXPHOS↓/glycolysis↑ in **human WWOX-KO cerebral organoids** — but by **transcriptome (n=2 WT vs n=4 KO, raw P<0.01)**, never flux. 🔴 **No Seahorse, no fluxomics, in any WWOX system** | **PARALLEL** in principle; the human limb argues it may not be present at all | Yes — a ketone bypass below the block (`R-05`) | 🟡 **Not a selectivity problem — a target-presence problem.** *"Human metabolism is normal, and it was checked four times"* (`DL-BIO-009`); the single MRS outlier reports cerebral lactate *"extremely low"*, the **opposite** of the prediction, in a patient with a confounding HSPG2 variant. And `H-2`/`DL-MECH-028`: WWOX binds HIF1α via **WW1**, not the SDR — so this lever may be worth **less** in a residual-protein class than in a null class |
| **G2** | **Systemic hypoglycaemia** | `DATO` — reversible by **CNS-only** neuronal restoration (`CLAIM 004`: *"ipoglicemia reversibile da restauro CNS-only (controllo centrale del glucosio)"*), **`Wwox`-null mouse** | **DOWNSTREAM OF THE NEURON** | Yes, and one exists: digoxin/HIF1α raised acute blood glucose in the null | 🔴 **FAILS** — `N-07`: cardiac glycoside, extremely narrow index, `REPORTED_DOSE_AMBIGUITY` unresolved, and the endpoint is a metabolic proxy with **no neurological readout anywhere in it** |
| **G3** | 🔴 **The peripheral, NON-glucose systemic phenotype — metabolic acidosis, uraemia, hypocalcaemia, leukopenia, splenic atrophy and thinned thymic cortex; osteopenia in a second model** | `DATO` — `CLAIM 036`, **systemic constitutive `Wwox^ΔCre/ΔCre` (EIIA-Cre) at P18**: bicarbonate 14.50±3.5 vs 21.67 mEq/L (`p=0.006227`), BUN 37.25 vs 17.67 mg/dL (`p=0.01086`), calcium 10.18 vs 11.13 mg/dL (`p=0.000385`), WBC 4.2 vs 9.45 ×10³/µL (`n=2/group`), spleen 0.21% vs 0.53% body weight (`p=0.0015`). Converging, **different species**: BUN and creatinine up in the **rat `lde/lde`** at 28 days, with **glucose, calcium, Na⁺, K⁺, Cl⁻ all non-significant** — `CLAIM 038` | 🔴 **GENUINELY UNRESOLVED, AND THAT IS THE POINT.** `CLAIM 038` holds **two competing explanations for the BUN, both `IPOTESI`, both never tested**: renal insufficiency (against: kidneys histologically normal, no proteinuria, no anaemia) **or seizure-driven hypercatabolism**. If the second is right this node is **downstream of the seizures**; if the first is right it is **independent of them**. Nobody has run the discriminator | 🔴 **NO INTERVENTION RECORD EXISTS.** `TX-001…TX-007` contain **zero** entries keyed to this phenotype; `R-01…R-09` contain zero; `HYP-*` contain zero (measured in §2.3) | **N/A — and that is the finding.** There is nothing to audit because nothing has been proposed. The first move here is a **measurement**, which has no selectivity problem at all |
| **H** | **DNA-damage-response / ATM competence** | `DATO + INFERENZA prudente`, `in observation` — `CLAIM 029`, **oncological/DDR cell contexts, not a paediatric CNS model**. Counter-directional qualification already recorded: in the only panel plotting `Wwox` WT beside KO, the **wild type carries the highest total mutation burden in the whole dataset**, WT and KO interleaving across the rank order (`PMID 41562193`) | **PARALLEL**, and prenatal/proliferative | 🔴 **No safe formulation exists.** `mechanism_intervention_map.md` §2.2 **refused it admission**: WWOX loss gives progenitor proliferation **with** loss of the apoptotic checkpoint (`DL-MOL-010`), so *"restoring checkpoint competence pharmacologically in a proliferative developmental compartment has no safe formulation"* | 🔴 **The direction is inverted before selectivity is even reached.** A perfectly selective agent here would still be pointed the wrong way for a developing brain |
| **I** | **Astroglial K⁺ / water homeostasis (Kir4.1/KCNJ10–AQP4)** | 🔴 **`IPOTESI` ×2, no mechanistic bridge** — `superior_node_search_20260922.md` NODE 2, explicitly **FLAG ONLY**. It would explain three unexplained repository facts at once: region-restricted extracellular vacuoles in CA1 and amygdala (**9/9 vs 0/10, rat `lde/lde`**, DG and CA3 spared); ataxia in **95% vs 0%** with **no marked cerebellar histopathology** (`CLAIM 039`); uraemia with histologically normal kidneys (`CLAIM 038`) | 🔴 **Would be UPSTREAM of the seizures if true** — K⁺ buffering failure is an excitability mechanism, not a consequence. **This is the only row in the table that could be upstream** | 🔴 No. Nothing has ever been applied | **N/A — nothing proposed.** The first move is a stain or a transcript lookup, not a drug |
| **J** | **Wnt/β-catenin hyperactivation; MYC ↑ in radial glia** | `DATO` for direction in **human WWOX-KO cerebral organoids** (nuclear β-catenin ~1.7×; WNT ligands/LEF1/AXIN2 up; partially recovered by W-AAV). MYC is the **top upregulated gene in radial glia** of WWOX-KO, WOREE and SCAR12 organoids | **PARALLEL**, and it is a **neurogenesis/corticogenesis** node ⇒ largely **prenatal** | Yes, and one arm exists — **A51** in human WWOX-KO organoids: SOX2⁺ and NEUN⁺ moved; 🔴 **SATB2⁺ `ns`, CTIP2⁺ `ns` — layer-neuron output NOT rescued** | 🔴 **FAILS on the source's own words.** A51 is *"a multi-kinase inhibitor … established to suppress Wnt **and** MYC"* — **the axis TX-004 names is not the axis the experiment isolates**. For the selective alternative, `R-03`: no approved Wnt/tankyrase inhibitor in paediatric neurology, BBB not established, and **intestinal-crypt and bone toxicity** are the classic liabilities |
| **K** | **Chloride gradient / `E_GABA`** | 🔴 **Not admitted as a node.** `R-07` is **T6**: *"no `E_GABA`, no intracellular chloride, no NKCC1/KCC2, no GABA response, no GABA pharmacology"* in **any** WWOX system. "Depolarising GABA" is the authors' `IPOTESI` read off a marker pattern | Unknown by construction | Bumetanide — unrankable | 🔴 **The sign of the effect depends on an unmeasured quantity.** Listed here so it is not mistaken for an omission |
| **L** | **Autophagy–lysosome flux** | 🔴 **Sign contested 2:1** — one source has WWOX ⊣ autophagy, one has WWOX activating it, and the human organoid transcriptome has **autophagy down and mTOR down simultaneously**, which is internally discordant | Unknown | — | 🔴 **An intervention whose sign is unknown is not a node; it is a coin toss with a safety cost.** Not carried forward |

### 1.1 · The three rows that matter most, read together

- 🔴 **Only ONE row (I) could be upstream of the seizures — and it rests on two consecutive `IPOTESI` links.**
- 🔴 **Every row with `DATO`-class evidence is either the seizure mechanism itself (C, D) or downstream of the
  neuron (E, F, G2) or parallel-but-prenatal (J, H).** This is `H-F1`, and it survived the check (§6).
- 🔴 **The row with no intervention record at all (G3) is the row with the most unmeasured consequence.**

---

## 2 · THE SELECTIVITY AUDIT — run as a gate, not as a caveat

> **The rule this section enforces, in the repository's own terms.** The laboratory has already had to correct
> itself on a drug whose standing came from the group that ran it rather than from what it hit: the GSK3β →
> seizure link *"rests entirely on one non-selective drug, with no molecular confirmation that the drug engaged
> the target in these animals, no second inhibitor, no genetic test, and no interaction test"*
> (`PHASE1_PMID32000863_SCIC_FIRSTPASS_v1`; the same defect is logged as *"no interaction test", "one
> non-selective drug", "no target engagement"* in `SCHEMA_GAPS_PER_EDGE_OUTPUT_SCIC_v1`). **A drug that hits a
> pathway WWOX touches is not thereby a WWOX therapy.**
>
> 🔴 **Provenance honesty.** The brief quotes this as *"Group standing does not repair a non-selective drug."*
> **I could not locate that sentence verbatim anywhere in the repository** (§7). The *adjudication* it names is
> real and is in the two files above plus `N-02` and `CLAIM 016`; the *sentence* is not. It is treated below as
> the correct rule with an unverified wording.

**The gate.** For each intervention: *what else does it hit, and at what relative potency?* **If the answer is
unknown, the intervention is not a candidate — it is a question.**

### 2.1 · The audit table

| Intervention | Node | What else it hits | Relative potency | Verdict under the gate |
|---|---|---|---|---|
| **Lithium** | A | Multi-target; and it **stabilises β-catenin**, i.e. it **activates** a pathway already hyperactivated (`DL-MOL-003`) | 🔴 **Not recorded anywhere in this repository** | ❌ **FAILS — twice.** It failed its genotype-specificity test in its own figure (all three genotypes, wild type included), and it is directionally conflicted across two admitted axes. Settled; not reopened |
| **An Axin-site GSK3β ligand** | A | Would block the docking site **generically** — `DIS-009` showed WWOX itself inhibits GSK3β-dependent phosphorylation of **GS-1, a glycogen-synthase peptide unrelated to Tau**, to ~18% of control (L404A ~87%) ⇒ **generic docking-site block, not substrate selectivity** | 🔴 Unknown — the molecule does not exist | ❓ **QUESTION.** The *isoform*-selectivity claim (`H-1`) is distinct from the rejected *substrate*-selectivity claim and is **`PREMISE: INFERENZA`, never measured on WWOX** |
| **Memantine** | C | Uncompetitive NMDAR open-channel block is the nominal action | 🔴 **This repository records no off-target profile and no potency ratio for memantine at all.** What it does record is the developmental liability: NMDAR signalling is **required** for activity-dependent maturation — *"the same processes WWOX loss already impairs"* (`R-02`) | ❓ **QUESTION, not candidate** — and the stronger objection is not selectivity but `N-15`: suppressing a network *state* is not correcting a *developmental* lesion |
| **d-APV** | C | Competitive NMDA-site tool compound | 🔴 Not recorded | ⚠️ **TOOL.** T1 for the tool in the S-KO slice; **not a therapeutic object** and must never be reported as one |
| **Carbenoxolone** | D | 🔴 **Documented in-repo: blocks NMDAR as well as pannexin**, and the effect *"did not return to normal levels after washout"* | Not recorded | ❌ **FAILS — non-attributable.** The textbook case: the node looked strong because the reagent was dirty |
| **BB-FCF** | D | Selective pannexin-1 blocker | — | ❌ **FAILS on result, not on selectivity.** The point estimate went the **wrong way** (`N-16`). 🔴 **A selective agent that returns a negative is more informative than a dirty one that returns a positive** |
| **Ethosuximide** | C-adjacent | Nominal target: T-type Ca²⁺ channels | 🔴 **The target has never been examined in this disease.** LEGEND's own measurement: `WWOX AND (CACNA1G OR CACNA1H OR CACNA1I OR "T-type" OR Cav3.1 OR Cav3.2 OR "calcium channel")` = **`total_count: 1`**, and that record is a **gene-list co-occurrence**, not a relationship | ❌ **ADJACENT, not selective for any node in §1.** It carries the field's **only** genotype-specific in-vivo pharmacology (`n.s.` in `+/+` and `+/−`, significant in `−/−`) — but the endpoint is a **provoked** convulsion, the discharge it would be predicted to hit **has never been measured as a frequency** (`Hz` = 0 in the whole body of the only paper reporting SWDs), and **it has already reached a WWOX-DEE patient, in a list of seven medications with *"No sustained positive effect"*.** Classified `SYMPTOMATIC`; `N-15` bars anything more |
| **Pro-myelinating agents (class)** | E | The class's promyelinating action is attributed to activities **other than** the nominal indication of its members | 🔴 Not recorded here for any member | ❌ **ADJACENT.** And `N-13`'s objection is upstream of selectivity: **wrong cell compartment** — the OPCs are present and not receiving the axonal signal |
| **Anti-neuroinflammatory (class)** | F | — | — | ❌ **UNAUDITABLE.** `R-06` names **no compound**; *"no compound is identifiable in the public record"*. A class label cannot be audited, and 🔴 *"the target is downstream of the target"* |
| **Ketone bypass** | G1 | No molecular target; acts by substrate supply | n/a | ⚠️ **NOT A SELECTIVITY PROBLEM — A TARGET-PRESENCE PROBLEM.** Human WWOX metabolism is **normal on four independent screens**; the real-world continuation signal runs against the rationale. The single remaining falsifier is already specified as `E-3` |
| **Digoxin** | G2 | Cardiac glycoside | Narrow index; `REPORTED_DOSE_AMBIGUITY` unresolved | ❌ **FAILS.** Correct **target validation**, wrong clinical object (`N-07`) |
| **A51** | J | 🔴 **Declared by its own source as suppressing Wnt AND MYC** | Not stated | ❌ **FAILS.** The only pharmacological rescue ever obtained in human WWOX-deficient neural tissue **cannot be attributed to the axis it is cited for** |
| **Tankyrase inhibitor** | J | Wnt/β-catenin | Not recorded | ❌ **ADJACENT + liability.** Intestinal-crypt turnover and bone toxicity; no paediatric-profiled candidate; BBB not established |
| **Bumetanide** | K | NKCC1 nominal; the diuresis is the family's other member | 🔴 Not recorded | ❌ **QUESTION at best.** Its load-bearing premise has **never been measured** in any WWOX system; poor CNS penetration is a known unsolved limitation |
| **mTOR inhibitors** | — | — | — | ❌ **Wrong direction** (`N-01`), with the weakness of the single dataset stated |
| 🔴 **Tau-lowering** | B | Selective — **that is the problem** | — | ❌ **PREDICTED HARMFUL.** Tau knockdown **abolished** the rescue in the primary. **A perfectly selective agent aimed at the wrong node is more dangerous than a dirty one, because it will work.** Credit: this negative was established earlier today in `superior_node_search_20260922.md`; it is reproduced, not re-derived |

### 2.2 · What the audit actually shows — three results, none of them a drug

1. 🔴 **Prediction `P-2` was confirmed without exception.** Across `disease-models/wwox/`, a case-insensitive
   sweep for `IC50 · Ki · selectivity ratio · fold-selectiv* · off-target potency` returns **five hits in the
   entire tree**, and **not one is a downstream-node therapeutic**: one is a glioma TMZ-IC50 confound, one is an
   abstract-depth IC50 with the subscript deleted by the extractor, and **three are the *declared absence* of a
   CDK7 fold-selectivity figure**. ⇒ **This repository does not currently hold a single documented selectivity
   ratio for any intervention at any node in §1.** By the gate, **every row in §1 yields a question, and none
   yields a candidate.**
2. 🔴 **Selectivity is necessary and not sufficient, and node B proves it.** BB-FCF (selective, negative result)
   and Tau-lowering (selective, predicted harmful) are the two cleanest cases in the file, and they point in
   opposite directions. The gate must therefore be **applied together with the direction check**, never instead
   of it.
3. 🔴 **Two nodes cannot be audited because nothing has ever been proposed at them — F (no compound) and G3, I
   (nothing at all).** For F that is a weakness. For **G3 and I it is the opposite**: their first move is a
   **measurement**, which carries no selectivity risk whatsoever, and that is precisely why they score as they
   do in §3.

### 2.3 · 🔴 The measured absence behind node G3

Prediction `P-1`, tested by grep across `therapeutic_strategies_current.md` and
`therapeutic_hypotheses_ledger_current.md` for `hypoglyc* · acidosis · bicarbonat* · h(a)ematopoie* · calcium ·
bone · osteo* · splenic · an(a)emi*`:

- **`therapeutic_strategies_current.md`: 1 hit** — and it is `TX-004`'s **safety line**, recording
  *"Wnt inhibitors: intestinal/bone toxicity"* — i.e. bone appears as a **liability of a CNS lever**, never as
  a target.
- **`therapeutic_hypotheses_ledger_current.md`: 1 hit** — and it is a **lexical false positive**, the word
  *backbone* inside a protein-folding argument.

⇒ **`TX-001`…`TX-007`, `R-01`…`R-09` and the entire `HYP-*` portfolio contain ZERO entries addressed to the
peripheral systemic phenotype.** It counts zero in the gene-therapy analyses because the vector is
neuron-restricted and the analyses score neurological endpoints; and it counts zero in the portfolio because
every portfolio entry was scored on a CNS endpoint. 🔴 **What the field calls a confounder (`CLAIM 036`: the
P14–P18 systemic null is *"ipoglicemico, acidotico, uremico e anemico"*) is, from the patient's side, an
untreated phenotype that nobody has scored.**

⚠️ **And the honest correction to my own framing, which refutes half of hypothesis `H-F3`:** the **glucose**
component is **not** outside the reach of a CNS lever — `CLAIM 004` records hypoglycaemia as **reversible by
CNS-only restoration**. So the node is **not** "the periphery, untouched". It is narrower and sharper: **the
NON-glucose components — bicarbonate, BUN/creatinine, calcium, WBC, spleen, bone — have never been measured
after ANY intervention in ANY WWOX system**, so **whether they are CNS-reversible is unknown in both
directions.**

---

## 3 · OUTCOME-WIDTH SCORING

> **The session's rule, applied literally.** An experiment's or an intervention's value is the **width of its
> outcome distribution**, not the importance of the quantity it targets. **A node whose outcome is foreseeable
> is a validation, not a discriminator.**
>
> **Operational test used below** (fixed before scoring, §6 DISCRIMINATOR): a node scores **WIDE** only if I can
> write down two outcomes of its cheapest experiment such that **the repository's existing content does not
> already make one of them the expected answer.**

| Node | Cheapest first question | Outcome if run — is it foreseeable? | **Width** | Why |
|---|---|---|---|---|
| **A** GSK3β kinase | Does an Axin-site ligand separate β1 from β2? | Genuinely open — never measured on WWOX | **MEDIUM–WIDE** | But it requires a molecule that does not exist, so the width is not purchasable cheaply |
| **B** Tau/microtubule polymer | Is pTau S396/S404 up and the polymerised:free tubulin ratio down in **isogenic human WWOX-KO** neurons vs parental? | 🔴 **Genuinely open.** Every measured link is in a **neuroblastoma line by over-expression or RNAi**; `CLAIM 035` states in its own words that **no WWOX-DEE allele has ever been tested**; the key assembly assay is **cell-free, on purified tubulin** | **WIDE** | The human limb — link L7 — is `INFERENZA` and is the **only** thing standing between the chain and a falsification |
| **C** NMDAR / E-I | Does NMDAR blockade reduce bursting in a WWOX-null system? | 🔴 **ALREADY ANSWERED.** d-APV drove spontaneous bursting to **zero**, reversibly | **NARROW** on the mechanism | **This is a validation, not a discriminator.** The open part is translational (*does an approved analogue do it, dose-dependently, without a developmental cost*) and is `E-9`, already specified |
| **D** Gap junction / pannexin | Repeat the pannexin arm? | Foreseeable — the selective agent already went the wrong way | **NARROW** | Re-running it validates a negative |
| **E** Myelin / OPC | Does pushing OPCs help when the axonal signal is absent? | 🟡 **Mostly foreseeable** — `N-13` predicts little. ⚠️ **But not entirely**: the oligodendrocyte-directed arm is **confounded by tropism on the authors' own admission** and partial benefit is **explicitly not excluded** | **NARROW–MEDIUM** | 🔴 This is where prediction `P-4` was **refuted** (§6): I predicted no residual equipoise and the repository records some |
| **F** Gliosis | Does damping gliosis change development? | 🔴 **Foreseeable.** Neuron-only rescue already reduces gliosis ⇒ it is an effect; and `N-15` says seizure/inflammation control is not development | **NARROW** | Treating an effect |
| **G1** Neuronal bioenergetics | Seahorse OCR/ECAR on donor-derived cells and on the existing organoids | Partly foreseeable — the human screens are normal ×4, so "normal" is the favoured outcome, but the organoid arm is untested | **MEDIUM** | Already specified as `E-3`; not displaced |
| **G2** Hypoglycaemia | — | Foreseeable — it is CNS-reversible | **NARROW** | Already answered |
| **G3** 🔴 **Peripheral non-glucose systemic phenotype** | **After neuron-restricted WWOX restoration, do bicarbonate, BUN/creatinine, calcium, WBC and spleen normalise?** | 🔴 **Completely open, in both directions, and nobody has ever asked.** **Normalise** ⇒ the entire systemic collapse is a **brain** phenotype and `CLAIM 036`'s confounder is itself neuron-driven, which re-reads a decade of null-mouse neuropathology. **Do not normalise** ⇒ there is a real peripheral disease that **every lever in the portfolio leaves untouched** and that **no analysis has ever scored** | 🔴 **WIDEST IN THE FILE** | Both outcomes are consequential, neither is favoured by anything in the repository, and the question has **never been posed** |
| **H** DDR/ATM | — | The intervention direction is inverted for a developing brain before any measurement | **NARROW (for intervention)** | Interesting biology, unusable direction |
| **I** Kir4.1 / AQP4 | Are KCNJ10/AQP4 abnormal in a WWOX-deficient system? | 🔴 **Completely open.** `Kir4`, `KCNJ10`, `AQP4`, `aquaporin`, `spongiform` return **zero files** across the whole `disease-models/wwox/` tree; `WWOX KCNJ10` = **1 PubMed record**, a gene-list co-occurrence | **WIDE** | ⚠️ But the chain has **two consecutive `IPOTESI` links**, so a positive would be a *beginning*, not a lever |
| **J** Wnt / MYC | Deconvolve A51 into selective MYC vs selective Wnt arms | Genuinely open (three live outcomes, including "neither") | **MEDIUM–WIDE** | 🔴 **Already named as Scientist B's single best next experiment.** Not re-proposed here |
| **K** Chloride / `E_GABA` | Gramicidin perforated patch | Genuinely open, and it decides an entire axis | **WIDE** | 🔴 **Already specified as `E-2`.** Not re-proposed here; it remains, in my reading, the highest-value unrun experiment in `mechanism_intervention_map.md` |
| **L** Autophagy | — | Sign unknown ⇒ not scorable | **N/A** | Parked |

🔴 **The scoring's own headline, and it is uncomfortable:** the node with the **best evidence in the file (C)**
scores **NARROW**, and the node with **no evidence of an intervention at all (G3)** scores **WIDEST**. That is
what the rule says, and I have not smoothed it.

---

## 4 · THE THREE BEST NODES, and the single cheapest first experiment for each

**Ranking metric, as set by the brief:** (tractability × informativeness) ÷ (risk × non-selectivity).

🔴 **Two nodes are excluded from the ranking on purpose, and not because they are weak.** `K` (chloride/`E_GABA`,
via `E-2`) and `J` (A51 deconvolution) are **already specified experiments owned by prior work**; re-proposing
them would be this file claiming another actor's experiment as its contribution. They stay where they are and
are **not displaced** by anything below.

🔴 **And the best-evidenced node, C (NMDAR / E-I), is deliberately NOT in the top three.** It has the highest
numerator term the repository can supply and it loses on every other term: its outcome is **foreseeable**
(d-APV already zeroed the bursting), its non-selectivity is **unrecorded**, its risk is **chronic NMDAR blockade
in a developing brain whose activity-dependent maturation WWOX loss already impairs**, and `N-15` caps what
correcting a seizure mechanism can buy. **Its open part is translational and is already `E-9`.**

---

### 🥇 FIRST — **G3 · the peripheral, non-glucose systemic phenotype**

**Why it wins.** Widest outcome distribution in the file (§3); **zero** portfolio coverage, measured (§2.3);
**zero** intervention risk at step 1, because step 1 is not an intervention; **no selectivity problem exists**,
because no molecule is involved; and it is the only node whose value does not depend on `N-15`, because it
never claimed a developmental endpoint in the first place.

> **The single cheapest first experiment — ANALYSIS-ONLY, no new material, no animal, no fetch.**
> **A denominator audit of peripheral analytes across every WWOX intervention arm ever run.** Take the
> intervention papers this repository has already read to `complete_fulltext_read` depth and whose locator
> manifests are on disk — the two neuronal gene-therapy studies, the PTZ pharmacology study, the organoid
> study — and, for each, record **which of bicarbonate/total CO₂, BUN, creatinine, calcium, WBC, spleen weight
> and bone was measured in ANY arm, treated or untreated.** The manifests, the dossiers and the deep-dive JSONs
> are local; this is a table-building exercise over material already held.
>
> **What it decides.** If the answer is **zero across all arms**, then the repository can state, as a measured
> fact rather than an impression, that **no WWOX intervention has ever been evaluated against the peripheral
> phenotype** — which converts §2.3's grep result into a defensible denominator and makes the next step
> (a standard clinical-chemistry panel on terminal blood from animals **already being generated** in any
> existing rescue cohort — one extra tube, no extra animal) a **justified** request rather than a speculative
> one. If the answer is **non-zero**, then the data to answer `CLAIM 036`'s confounder question **already
> exist unextracted**, which is the better outcome and costs nothing to discover.
>
> ⚠️ **Bounds, stated so the result cannot be over-read.** (i) `CLAIM 036`'s analytes come from the **EIIA-Cre
> systemic null**; the rescue arms are in **different `Wwox`-null strains** with a **neuron-restricted**
> vector — a cross-model comparison, and the `MECHANISM_TRANSFER_FIREWALL` applies. (ii) `CLAIM 038` shows the
> **rat `lde/lde`** is **uraemic without being hypoglycaemic** — *the opposite profile* — so "the peripheral
> phenotype" is not one thing across species. (iii) `CLAIM 036`'s own `REVIVAL_TRIGGER` is still open: **brain
> WWOX ablation was never shown in that model.** None of this blocks the audit; all of it bounds its reading.

---

### 🥈 SECOND — **B · Tau's microtubule-binding competence (the polymer, not the kinase)**

**Why it is here.** Six `DATO` links; the target process — dendritic and axonal arborisation — is one of the
very few still running at the age WOREE children present (seizure onset at a **median of 5 weeks**;
`postdiagnosis_window_evidence_20260922.md`); it composes with every restoration lever rather than competing;
and it carries a **pre-emptive negative** that protects the field from the obvious wrong move.

🔴 **Attribution.** The node and its killer experiment were established **earlier today** in
`superior_node_search_20260922.md` §3 NODE 1. **I am not claiming them.** What follows is that experiment plus
**one design change**, which is this file's only contribution to it.

> **The cheapest first experiment — existing lines, one differentiation, three blots.**
> In **isogenic human WWOX-KO neurons or cortical organoids versus the parental line** (both exist, `DL-MOL-010`),
> measure on the same lysates: **(a)** pTau **S396 and S404** — 🔴 **never** phospho-GSK3β-S9, which `CLAIM 035`
> establishes returns a **false negative** on this axis; **(b)** the **polymerised : free tubulin ratio** by
> standard fractionation; **(c)** MAP2.
>
> 🔴 **My one addition, and the reason to make it: run the same three readouts in parallel on the SDR-missense
> comparator line the same laboratory already holds (`G372R`) and, where available, on `P47T` material.** The
> node makes a **falsifiable differential prediction** that the two-arm version cannot test: it should be worth
> **least** in a class that retains folded protein containing 388–407. **`P47T` has normal protein levels and
> is mild** (`CLAIM 030`). So: if the polymer defect is **as large** in a retained-protein allele as in the
> null, the node's genotype logic is **false** and the effect is not running through the WWOX→GSK3β→Tau arc.
> **This converts a confirmation into a discriminator and supplies its own negative control** — which is
> exactly what `E-8` argues for on the abundance axis and what nobody has argued for on this one.
>
> **What kills the node:** pTau S396/S404 unchanged **and** the polymerised fraction unchanged versus isogenic
> control. That falsifies link L7 at its only human point and the node is dead. **A good outcome, cheaply.**
>
> ⚠️ **Bounds.** `G372R` is a **natural-variant comparator, not a validated negative control**
> (`MECHANISM_TRANSFER_FIREWALL`); `P47T` is a **different domain and a different lesion** and is not a
> read-across bench. The rat MAP2 datum (L6) comes from an animal `CLAIM 038` records as **uraemic**. And the
> WWOX↔Tau **binding** question is `INDETERMINATO` (`DIS-010`, `D-14`) — which **does not bite here**, because
> this chain runs WWOX → GSK3β → Tau and requires no direct WWOX–Tau binding.

---

### 🥉 THIRD — **I · astroglial K⁺ / water homeostasis (Kir4.1/KCNJ10–AQP4)**

**Why it is here despite being the weakest chain in the file.** It is the **only** node in §1 that could be
**upstream of the seizures**; it would explain **three unexplained repository facts at once** (regional
vacuolation, unexplained ataxia, uraemia with normal renal histology); its surface is **untouched in both
directions**; and its first step costs almost nothing and carries no intervention risk. 🔴 **It is ranked third
and flagged, not scored — two consecutive `IPOTESI` links, and the repository has already been burned once by
a lead of exactly this shape** (*"Both halves are true and the bridge does not exist"*).

🔴 **Attribution.** The node and the staining experiment are from `superior_node_search_20260922.md` §3 NODE 2.
**My contribution is a cheaper step that comes before it.**

> **The cheapest first experiment — ANALYSIS-ONLY, on a public dataset already re-analysable.**
> Before asking anyone for archived `lde/lde` sections, **re-interrogate the existing human WWOX-KO cerebral
> organoid transcriptome (GEO `GSE156243`, already named as a re-analysable benchmark in
> `mechanism_intervention_map.md`) for `KCNJ10`, `AQP4` and the astroglial gap-junction transcripts.**
> Cost: a dataset the repository already points at, no new material, no correspondence.
>
> **What it decides.** A **clear abnormality** in human WWOX-null neural tissue converts link L4 from `IPOTESI`
> to a measured direction and **justifies the staining request**. **No signal** does **not** kill the node —
> and saying so is the whole discipline here.
>
> 🔴 **Why a null there is weak, stated before the experiment rather than after it.** (i) Cerebral organoids at
> the stages profiled are **astrocyte-poor**, so a glial transcript can be absent for reasons of composition,
> not biology. (ii) The dataset is `n=2` WT vs `n=4` KO with EV selection at **raw `P<0.01`**, and **five gene
> symbols are corrupted by spreadsheet auto-dating** — both already recorded. (iii) The phenotype it is meant to
> explain is a **rat `lde/lde`** phenotype, and the transcriptome is **human organoid**: two species, two
> systems, and `MECHANISM_TRANSFER_FIREWALL` applies in both directions. ⇒ **A positive is informative; a
> negative is uninformative, and must be reported as `INCONCLUSIVE`, never as a refutation.** Only then does
> the staining run become worth requesting.
>
> ⚠️ One datum argues against the node before anyone spends a day on it, and it is already recorded: the
> authors of the vacuolation study explicitly **contrasted** their lesion with the widespread spongy
> degeneration of two other rat strains — they had the diffuse-spongiform analogy in front of them and
> **rejected it**.

---

## 5 · 🔴 WHAT THIS WHOLE AXIS CANNOT DO

Stated plainly, because the value of §1–§4 depends on none of it being over-read.

1. **A downstream intervention does not restore WWOX.** Every node in §1 is a *consequence*. Nothing here
   returns the protein, corrects the allele, or changes what is written in the gene. The only levers that act
   at the level at which the disease is written are gene addition and the allele-level chains, and they are
   **not** in this file.
2. **It does not address the primary lesion, and it may be symptomatic at best.** `N-15` is the most
   consequential negative in the portfolio and it governs this entire file: in published WWOX children,
   cognitive and psychomotor impairment **precedes** the epileptic encephalopathy and **does not improve** when
   epileptic activity is controlled — *"the developmental outcome was unfavourable with profound impairment
   **despite improvement of epileptic activity**"*. In one case the spasms **resolved** and the child was
   profoundly delayed at two years. 🔴 **Seizure control remains fully indicated for quality of life, status
   epilepticus, SUDEP, sleep and manageability — and must never be scored as disease modification.** Limits:
   N=2, observational, uncontrolled.
3. 🔴 **WWOX loss is developmental, so a postnatal downstream intervention inherits the timing question the
   repository has already flagged for gene therapy — and inherits it in a WORSE form.** The gene-therapy window
   is **P0–P5 in mouse**, with post-natal dosing **explicitly future work**; neuronal restoration rescues
   excitability and function but does **not** repair the progenitor/radial-glia defect, which is largely
   prenatal. A downstream lever arrives **later still** and acts on a **narrower** slice of biology. And the
   quantity the whole timing argument turns on **does not exist**: *"Nobody has ever measured the age at which a
   WOREE child is diagnosed"* — the PubMed census `WWOX AND "age at diagnosis"` returns **`total_count: 0`**.
   What is measured is presentation: seizures begin at a **median of 5 weeks**. ⇒ **Any post-diagnosis
   intervention acts at or after ≈1–2 months of postnatal life, with no measured upper bound.**
   ⚠️ The counterweight, and it is real: the human brain at that age is **not** developmentally quiet — the
   postnatal subventricular zone still carries radial-glia-like cells and a dense DCX⁺ migratory network, and
   myelination runs for decades. 🔴 **But the WWOX limb of that cell is empty: nobody has ever looked at WWOX in
   postnatal human SVZ, the rostral migratory stream, or the medial migratory stream.**
4. **It cannot be scored as genotype-agnostic.** `H-2` / `DL-MECH-028` / `DL-MECH-008`: WWOX binds HIF1α via
   **WW1** and sequesters DVL2 via the **WW scaffold** — neither via the SDR. A residual-protein class may
   leave the metabolic and Wnt axes **partially preserved**, so those levers may be worth **less** there than
   in a null class. **Only gene addition is genotype-agnostic.** The same asymmetry, inverted, applies to node
   B: it is worth least in the class that keeps folded protein containing 388–407.
5. **It cannot be run on a compound genotype by extrapolation.** Every row in §1 carries its model and its
   allele. `Wwox`-null (two targeting strains), `S-KO`, `N-KO`, `P47T`, rat `lde/lde`, human WOREE and human
   SCAR12 are different objects, and the `gt/gt` hypomorph carries **no brain WWOX quantification and no
   neurological phenotyping at all**.
6. 🔴 **And it cannot yield a candidate today.** §2.2: this repository holds **no documented selectivity ratio
   for any intervention at any node in §1**. Under the gate the brief set, **every row yields a question.**

---

## 6 · THE PROSPECTIVE TRACE, WITH SCORES

**Persisted before any confirmatory search**, to
`scratchpad/TRACE_scientistF_20260922.md`, **written 2026-09-22 14:17:08 UTC**. Only the baseline enumeration
(`find` + `grep`, §0) preceded it. Reproduced here verbatim in substance, with outcomes appended **after** the
confirmatory pass. **No prediction below was written or altered after seeing its evidence.**

### OBSERVATION
`O-1` a bounded census of WWOX-independent **interventions** already exists (4 positive arms in the whole
literature). `O-2` GSK3β/lithium is already adjudicated in eight places. `O-3` the mechanism→intervention map
does not classify nodes as upstream/downstream of the seizures and does not score outcome width. `O-4` `N-15`:
cognitive impairment precedes the epilepsy and does not improve with seizure control. `O-5` `CLAIM 036`: the
systemic null at P14–P18 is metabolically decompensated.

### DIVERGE — six mechanistically distinct routes
`D-1` restore the brake's **output**, not the brake (occupy the Axin docking site with a non-WWOX ligand).
`D-2` clamp the **network state** at the receptor. `D-3` **bypass a metabolic block** by delivering carbon
below it. `D-4` supply the **missing non-cell-autonomous signal** to the OPC directly. `D-5` remove a
**secondary amplifier** (glia) to slow rather than correct. `D-6` **treat the periphery, not the brain** — the
systemic components that count zero in every gene-therapy analysis.

### CONNECT
`C-1` D-1…D-5 all sit at or below the seizure; **D-6 sits entirely outside that axis**, so `N-15` does not bound
it — because it never claimed development. `C-2` 🔴 **the three axes with the strongest node evidence are
exactly the three whose interventions are least selective**: node strength and intervention selectivity are
**anti-correlated** in this field. `C-3` `O-5` and `D-6` are the same fact seen twice — what the literature
calls a confounder is, from the patient's side, an untreated phenotype.

### HYPOTHESIS
`H-F1` no node will be simultaneously (a) `DATO`, (b) upstream of the seizures, and (c) selectively addressable.
`H-F2` the widest node will **not** be the best-evidenced one; it will be one where the repository records a
**missing measurement** rather than a measurement. `H-F3` the peripheral node will score highest and will be
**absent** from the portfolio.

### PREDICTION → RESULT → GRADE

| # | Prediction (made before the confirmatory pass) | Result | Grade |
|---|---|---|---|
| **P-1** | A search for an intervention record keyed to the peripheral phenotype returns **zero** `TX-*` and **zero** `R-*` entries | ✅ **CONFIRMED.** Two hits total across both portfolio files: a **Wnt-inhibitor bone-toxicity liability** and a lexical false positive (*backbone*). Zero targets | **A.** Specific, falsifiable, cheaply checked, and it carries §2.3 and the §4 first place |
| **P-2** | For **every** intervention nameable at a downstream node, at least one of {what else it hits, relative potency} will be **unknown** in this repository | ✅ **CONFIRMED WITHOUT EXCEPTION.** Five `IC50/Ki/fold-selectiv*` hits in the whole `disease-models/wwox/` tree; none is a downstream-node therapeutic; three are the **declared absence** of a fold-selectivity figure | **A.** It was falsifiable by a single documented ratio and none exists. It is what turns §2 into a gate |
| **P-3** | The DDR node will be non-actionable in the required direction | ✅ **CONFIRMED** — but the repository states this **explicitly** at `mechanism_intervention_map.md` §2.2 | 🔴 **C.** A cheap prediction about content the repository already answers in one sentence. It cost nothing and taught nothing. **Penalised** |
| **P-4** | The myelin node will be **NARROW** because `N-13` already predicts the outcome, i.e. the repository records **no equipoise** | 🔴 **REFUTED — and this is the file's best outcome.** `N-13` is explicitly *"not `refuted`"*; the oligodendrocyte-directed arm is **confounded by tropism on the authors' own admission**; *"partial benefit is not excluded"*; and a cell-autonomous oligodendroglial role is **in observation**. ⇒ Node E re-scored **NARROW → NARROW–MEDIUM** in §3, **after** the refutation, and recorded there as such | **A.** A refuted prediction that changed a score |
| **P-5** | Tau will **fail as a node**, because the WWOX–Tau binding question is `INDETERMINATO` | 🟡 **CORRECT LETTER, WRONG CONSEQUENCE — a near-miss that would have cost the file its second-place node.** Tau **does** fail as a *binding partner* (`INDETERMINATO`; **struck from the design** in `wwox_engagement_partner_adjudication_20260922.md` A-3) — **but it survives, and matters, as the downstream effector readout of the GSK3β arc**, and the strongest chain in §1 is built on exactly that. Acting on my prediction would have deleted node B | 🔴 **D.** The prediction was under-specified: it conflated *partner* with *effector*, two things this repository keeps separate. Recorded as a **named failure mode of my own reasoning** |

### HYPOTHESIS GRADES

| # | Outcome |
|---|---|
| `H-F1` | ✅ **CONFIRMED.** §1.1: the only possibly-upstream row (I) rests on two `IPOTESI` links; every `DATO` row is the seizure mechanism, downstream of the neuron, or parallel-but-prenatal |
| `H-F2` | ✅ **CONFIRMED.** The widest node (G3) is a **missing measurement**, and the best-evidenced node (C) scores **NARROW** |
| `H-F3` | 🟡 **HALF-CONFIRMED, HALF-REFUTED.** The portfolio-absence half is confirmed (§2.3). The mechanism half is **wrong**: hypoglycaemia is **CNS-reversible** (`CLAIM 004`), so the node is not "the periphery, untouched" — it is the **non-glucose** components, whose CNS-reversibility is **unknown in both directions**. The node survived the correction **narrower and sharper** |

### DISCRIMINATOR (fixed in advance, and it is what §2 enforces)
> *Does the repository record, for the named intervention, what else it hits and at what relative potency? If
> no → the node yields a question, never a candidate, regardless of how good the node's evidence is.*
> **This is the operational form of the rule the brief names: node standing does not repair a non-selective
> drug any more than group standing does.** Secondary discriminator for §3: a node scores WIDE only if two
> outcomes of its cheapest experiment exist that the repository's content does not already decide.

**Trace self-score: 3 × A · 1 × C · 1 × D, with one prediction refuted and one hypothesis half-refuted.**
Two predictions (`P-3`, `P-5`) were weak, and `P-5` was weak in a way that would have deleted a node.

---

## 7 · `REVIVAL_TRIGGER`s AND `COULD NOT ESTABLISH`

### 7.1 · `REVIVAL_TRIGGER`s opened by this file

Nothing is rejected here silently. These attach to **this file's own scoring**, not to any canonical record.

| Node / judgement | What would reopen or overturn it |
|---|---|
| **G3 scored widest** | Any WWOX intervention arm, in any model, reporting **bicarbonate, BUN/creatinine, calcium, WBC, spleen weight or bone** in a treated group. One such table collapses the width to a measurement |
| **G3's unresolved seizure relation** | A test of `CLAIM 038`'s two competing explanations — creatine kinase and muscle mass measured **in parallel** with BUN, in the same animals — which would classify the node as downstream-of-seizures or independent of them |
| **C excluded from the top three** | A memantine (or other approved NMDAR-antagonist) **dose–response on MEA** in WWOX-null neurons/organoids with parental **and** rescue lines as internal comparators (`E-9`), **plus** any recorded off-target profile. Either alone re-ranks it; both together move it to first |
| **F scored NARROW / unauditable** | A **named compound** for `R-06` — the class currently has none — **or** evidence that gliosis is an independent driver rather than an effect, i.e. a gliosis measure that does **not** fall under neuron-restricted rescue |
| **E scored NARROW–MEDIUM** | An **oligodendrocyte-directed rescue arm with demonstrated oligodendroglial transduction**, which is exactly what the confounded arm lacks; or any remyelination-stress result showing a cell-autonomous oligodendroglial WWOX role |
| **H (DDR) excluded** | A DDR-axis intervention with a **safe direction in a proliferative developmental compartment** — i.e. one that does not restore an apoptotic checkpoint in dividing progenitors |
| **I ranked third on two `IPOTESI` links** | Any measured abnormality of `KCNJ10`/Kir4.1 or `AQP4` in **any** WWOX-deficient system. Symmetrically: normal Kir4.1 and AQP4 abundance **and** normal perivascular localisation in the vacuolated region would close it |
| **B's genotype logic** | The `G372R`/`P47T` comparator arm proposed in §4 returning a polymer defect **as large** as the null's would falsify the node's genotype asymmetry — and, with it, the arc it is built on |
| **A (GSK3β) left as `ADJACENT`** | WWOX and the 388–407 peptide tested **against β1 and β2 in parallel** (`H-1`'s decisive test). A measured isoform preference converts an adjacency into a selectivity |
| **L (autophagy) left unscorable** | Clamped autophagic flux (LC3-II ± lysosomal block, with p62) in isogenic human WWOX-KO neurons versus parental. **Until a sign returns, it is not a node** |
| **The `gt/gt` hypomorph's absence from §1** | Any brain WWOX quantification or neurological phenotyping in that model. Its absence here is a **missing measurement**, never evidence |

### 7.2 · `COULD NOT ESTABLISH`

| # | What I could not establish | Why, and what it would take |
|---|---|---|
| **CNE-1** | 🔴 **The verbatim sentence *"Group standing does not repair a non-selective drug."*** A case-insensitive sweep for `group standing`, `non-selective drug` and `repair a non-selective` across the whole repository returns the **adjudication** (`PHASE1_PMID32000863_SCIC_FIRSTPASS_v1`; `SCHEMA_GAPS_PER_EDGE_OUTPUT_SCIC_v1`; `N-02`; `CLAIM 016`) and a **related but different** lesson (`2026-09-09_scientist-b-wave5.md` Q6: *"Not standing — **genre** did"*). **The rule is real; the quoted wording is not located.** Would take: the brief's own source, or a pointer to the file that carries it |
| **CNE-2** | Whether the peripheral analytes were measured in any WWOX **intervention** arm. §2.3 establishes they are absent from the **portfolio**; it does **not** establish they are absent from the **papers**. That is precisely what §4's first experiment is for, and I did not pre-empt its answer |
| **CNE-3** | Any relative-potency figure for any intervention in §2. Five `IC50/Ki/fold-selectiv*` hits exist in the tree and **none applies**. 🔴 **I did not go outside the repository to find one** — no fetch was made in this act, so this is a statement about **this repository**, never about the pharmacology literature |
| **CNE-4** | Whether node **I**'s transcripts are abnormal in human WWOX-null neural tissue. The dataset is named and re-analysable; **the re-analysis was not run here** and is proposed, not reported |
| **CNE-5** | Whether the `lde/lde` regional vacuolation has **any** mechanistic explanation. `CLAIM 037` carries the finding; the authors call the regional restriction unprecedented; **nothing anywhere explains it**, and I did not explain it either |
| **CNE-6** | The **frequency** of the spike-wave discharge in any WWOX model. Prior LEGEND measurement: `Hz` occurs **zero times** in the entire body of the only paper reporting SWDs. Every T-type/absence-mechanism argument in §2 is bounded by this and none of it is mine |
| **CNE-7** | Whether node **B**'s chain holds in **any** human WWOX-DEE allele. `CLAIM 035` states it in its own words: *"nessun allele WWOX-DEE è stato testato."* Every measured link is in a neuroblastoma line by over-expression or RNAi |

---

## 8 · SELF-GRADE

| Dimension | Grade | Reasoning |
|---|---|---|
| **Baseline enumeration (list-then-grep)** | **A−** | Listed first, grepped across everything listed, found the prior downstream census, the mechanism map and today's two sibling files **before** writing, and located the GSK3β/lithium adjudication in eight places without re-deriving any of it. −: I did not read `discovery_ledger_current.md` end to end, only the sections other files pointed at |
| **Non-duplication** | **B+** | §0.1 states the delta explicitly; nodes B and I are **attributed** to `superior_node_search_20260922.md` and contributed to rather than re-proposed; `E-2` and the A51 deconvolution are **deliberately left with their owners**. −: §1's rows A, C, E, F, G1, G2, J are largely re-presentations of `mechanism_intervention_map.md` in a different key. The **key** is new; most of the **content** is not |
| **The selectivity audit (§2)** | **A−** | Run as a gate with a stated pass/fail rule, applied to 16 interventions, and it produced a result that constrains the whole file (**no documented selectivity ratio exists here for any of them**) plus one genuine inversion (**a selective agent at the wrong node is more dangerous, not less**). −: for several compounds I could only record *"not recorded in this repository"*, which is honest but thin |
| **Outcome-width scoring (§3)** | **B+** | Applied literally, with the test fixed in advance, and it cost me the best-evidenced node — which is the sign it was applied rather than decorated. −: the WIDE/MEDIUM/NARROW scale is ordinal and unvalidated; two adjacent rows could swap without any rule being broken |
| **The three choices (§4)** | **B+** | Each first experiment is analysis-only or existing-material, each states what kills it, and each carries its bounds **before** the result. −: choice 1's cheap step is an **audit of what has been measured**, not a measurement — defensible, and one rung further from biology than the brief may have wanted |
| **Prospective trace (§6)** | **A−** | Persisted with a verifiable timestamp before any confirmatory search; six distinct routes; five falsifiable predictions; **one refuted, one hypothesis half-refuted, both recorded with the score changes they forced**. −: `P-3` was cheap and `P-5` was under-specified in a way that would have deleted node B — both penalised in the table rather than in prose |
| **Epistemic discipline** | **A−** | `DATO`/`INFERENZA`/`IPOTESI` separated in every row; alleles and models never pooled; every zero attributed to the prior session that measured it; no figure-panel claim made from an environment that cannot open figures; `PREMISE_TAG`s carried where the sources carry them; seven `COULD NOT ESTABLISH` items, one of which is the brief's own quotation |
| **BLOCK-1 compliance** | **A** | No dose, no route, no schedule, no clinical framing anywhere. Every compound is a mechanistic hypothesis. No canonical file, registry, queue, ledger, receipt or state manifest touched; no `BATCH_COMMIT`; no git command run; no external contact; no purchase; no clinical recommendation — `HUMAN_REQUIRED` |
| **🔴 Overall** | **B+** | The file does what the brief asked and its two strongest outputs are both **negatives**: that **no intervention at any downstream node in this repository has a documented selectivity profile**, and that **the widest-outcome node in the disease has never been proposed by anyone, including this repository**. It does **not** produce a therapy, a candidate, or a lead that could be acted on, and it should not be read as doing so. **Nothing is graded F.** |

---

**End.** Not medical advice. Read-only toward every canonical file, registry, queue, ledger, receipt and the
state manifest. Nothing promoted, nothing committed, no receipt claimed. Every compound named is a mechanistic
hypothesis and material for discussion with a treating clinical team — `HUMAN_REQUIRED`.

---

# ORCHESTRATOR VERIFICATION — 2026-09-22

## V1 · 🔴 CNE-1 is REFUTED — the sentence exists, verbatim, and where it hides is a NEW failure mode

`CNE-1` reports that *"Group standing does not repair a non-selective drug"* could not be located,
and treats the brief's wording as unsourced. **It is in the repository, word for word:**

> `disease-models/wwox/research/deepdive_manifests/PMID32000863.json:49`, inside the `waived` field:
> *"The pharmacology is the weak layer and is where this reading disagrees with the paper's own
> interpretation; see locators 1 to 4. **Group standing does not repair a non-selective drug.**
> NOTE: the waiver is per-section but the impediment is per-field."*

🎯 **Why the sweep missed it, and this is worth more than the correction.** The sentence sits inside
a **JSON string field in a `.json` manifest**. A sweep scoped to Markdown — `--include=*.md`, the
default reflex in this repository because the prose lives there — cannot see it. The delegate did
the right thing three times over (it searched three phrasings, it found the *adjudication*, and it
declared the wording unlocated rather than inventing a citation) and still reached a false negative,
because the **search surface** excluded the file type the sentence lives in.

🔴 **NINTH failure mode, added to this corpus's catalogue:**

> **A phrase inside a JSON string field is invisible to a file-type-scoped grep.** The eight
> existing modes are all about *query* construction; this one is about *corpus* scope, and it is the
> first of its kind. The repository's reasoning lives in `.md`, but its **attestations,
> manifests, locator sets and receipts live in `.json` and `.jsonl`** — which is precisely where a
> load-bearing sentence is most likely to have been written down once and never repeated.

🔴 **And the consequence is not confined to this file.** Every `--include=*.md` census run in this
session inherits the same blind spot, including delegate work I have already verified and landed.
None is retracted on that basis — a census is not wrong because its scope was narrower than ideal —
but **any absence asserted from a Markdown-only sweep is now bounded**, and re-running the load-
bearing ones across `.json`/`.jsonl` is cheap. **Standing rule adopted: a repository absence claim
must state its file-type scope, or be run unscoped.**

🟢 **Credit where it is due:** `CNE-1` is a delegate publicly doubting a rule its orchestrator handed
it as law, and saying so in the file rather than quietly complying. That is the behaviour that made
the new failure mode findable. The conclusion was wrong; the instinct was right.

## V2 · The pharmacology is verified verbatim against Breton 2021

I hold `PMC8609180` from my own retrieval. According to PubMed,
[DOI](https://doi.org/10.1016/j.nbd.2021.105529):

| Claim | Verdict |
|---|---|
| d-APV **eliminated** spontaneous bursting, reversibly | 🟢 *"Blocking glutamatergic neurotransmission with d-APV (50 μM) eliminated the spontaneous bursting events… Upon washout, the frequency, duration and peak-to-trough amplitude returned to normal."* |
| CBX effect **survived washout** | 🟢 *"CBX (100 μM) decreased the frequency of the events by 87% … and their duration by 18% … **This did not return to normal levels after washout.**"* |
| CBX is **not selective** — it blocks NMDAR too | 🟢 The paper says so itself: *"CBX may not be specific to gap junctions. First, it could block NMDA receptors … which could partially account for our observations."* |
| BB-FCF is the selective tool and its result is **negative** | 🟢 *"application of a specific Panx-1 blocker, BB, had minimal effect on the network excitability"* |

🟢 **So the selectivity audit's two cleanest cases are both first-hand verifiable**, and the
asymmetry the file draws from them is real: the **selective** tool gave a negative and the
**non-selective** one gave the positive that a naive reading would have banked.

## V3 · 🎯 The Tau inversion is correct, and it is the most useful thing in the file

`§2` predicts that **Tau-lowering would be harmful here** — the opposite of the intuition imported
from Alzheimer's. I verified the basis in Wang 2011 (`PMC3354054`,
[DOI](https://doi.org/10.1038/cdd.2011.188)): *"the neurite outgrowth stimulated by RA was abolished
when Tau was knocked down"*, and *"**Neither WWOX overexpression nor GSK3β knockdown promoted
neurite outgrowth in the Tau knockdown condition**, indicating that Tau is the effector of both
WWOX and GSK3β."* 🟢 **VERIFIED.**

**Tau is the effector through which the WWOX benefit is delivered.** A Tau-lowering agent would
therefore remove the substrate the rescue acts on. 🔴 **This is the strongest argument in the
session for the file's own thesis that selectivity is necessary and not sufficient: a perfectly
selective anti-Tau agent at this node would work, and working is the problem.**

## V4 · Endorsed

🟢 **The exclusion of the best-evidenced node** (NMDAR/E-I) on the ground that its outcome is
**foreseeable** — d-APV already zeroed the bursting, so a repeat is a validation and not a
discriminator — is the session's `outcome_distribution_width` rule applied by a delegate,
unprompted, **against** the row that would have looked strongest in a summary.
🟢 **The `IC50` / `Ki` / selectivity-ratio sweep returning five hits in the entire tree, three of
them the *declared absence* of a fold-selectivity figure**, is the kind of number that settles an
argument. Under the gate, **every node yields a question and none yields a candidate** — and the
file says so rather than promoting the least-bad row.
🟢 **`P-5` graded `D` against itself**, with the failure mode named: acting on its own prediction
would have deleted its own second-place node.
🟢 **GSK3β/lithium found already adjudicated in eight places and reproduced as a pointer only** —
the baseline enumeration done properly, by a delegate, on the first attempt.
⚠️ The peripheral analyte values (bicarbonate 14.50 vs 21.67 mEq/L, BUN 37.25 vs 17.67) are carried
as the file's attestation; I have not re-read that primary. They bear directly on the
`DISCOVERY_TRACE` cycle-1 `D3` question and should be verified before any use.

## V5 · Information gain and grade

**INFORMATION GAIN: MEDIUM–HIGH.** It produces **no candidate**, which is the correct output, and
its two strongest results are negatives: only one node could be upstream of the seizures and it
rests on two consecutive `IPOTESI` links; and no downstream intervention in this model has a
recorded selectivity figure. It also found a ninth search failure mode by being wrong in public.

**Grade: B+ endorsed.** **BLOCK-1 respected throughout** — no dose, no route, no schedule, nothing
framed as treatment, and the compounds named are mechanistic hypotheses only.

**No row is canonical; none is proposed for `BATCH_COMMIT`.** Nothing here is medical advice.
