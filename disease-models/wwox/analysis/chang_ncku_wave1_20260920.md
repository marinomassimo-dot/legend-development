# SCIENTIST_CHANG_NS_WWOX_NEUROPROTEOSTASIS_AND_PEPTIDE_INTERVENTION — Wave 1

**Date:** 2026-09-20 · **Papers processed:** 8 (6 receipted this wave, 2 read at abstract depth from
metadata) · **Receipts:** `FTR-20260920-{26355344,27551439,29067327,31752354,36498839,41677633}-01`,
chain verified at 162. Non-canonical analysis file. No canonical file edited, no gate created.

> 🔴 **Declared acquisition ceiling for this wave, stated before any finding.** This environment's
> network policy denies `eutils.ncbi.nlm.nih.gov` and `ebi.ac.uk` (agent-proxy `403 CONNECT`,
> logged), and `tool_preflight.py` reports `fitz`, `pdftotext`, `pdftoppm`, `pdfimages` all absent.
> So **no JATS deposit and no figure image is obtainable here**, `genre_discriminator.py` cannot be
> run, and the MCP text extraction additionally **strips figure callouts and reference markers**,
> leaving bare `()`. Consequence: **not one finding below is anchored to a figure panel**, and per
> `D-14` no negative asserted by a figure is adjudicated in this wave. Everything below is a
> prose-level fact — which is sufficient for genre, causal direction, method class, internal
> consistency and WWOX-dependence, and insufficient for anything resting on a panel.

---

## 0 · The finding that reorganises the batch: P1 and P2 are one paper and its own press release

`PMID 26355344` is **not a primary source and not an independent second source.** It is a
**News & Commentary** piece in *Cell Death & Disease*, authored by the Chang lab (Sze CI first,
Chang NS senior), about the Chang lab's own primary paper `PMID 27551439` in *Cell Death Discovery*.
Its own body identifies it: *"In an inaugural issue of [Cell Death Discovery], Chang described a
protein aggregation cascade…"*

Mechanically: PubMed article types `["News", …]`; no abstract; **5,029 bytes of deposit against
29,813 for the primary — a 5.9× ratio**; no Methods, no Results, no figure, no data of its own.

🔴 **Registry consequence.** `CORPUS P395` / `LIT-0395` carry it as `Tier B`, *"secondary full-text
target"*, `clinical relevance: MODERATE`, `Primary pathway: P5 — metabolism / mitochondria / redox`.
That tier would have credited the lab with **two convergent sources where there is one**, and the
scouting note that opened this batch listed both as first-wave mechanistic papers. It is the
`D-15` family — a secondary source counted as evidence for what it only restates — reached from a
new direction: here the secondary source and the primary source have **the same senior author**.

---

## A · Mechanistic chain — only what survives the primary evidence

| # | Arc | Verdict | What the primary actually shows |
|---|---|---|---|
| 1 | WWOX loss → TPC6AΔ aggregation | **PARTIAL** | Direction is right but the evidence class is thin. In `27551439` the ordering claim (*"TPC6A knockdown induces TIAF1 aggregation, whereas TIAF1 knockdown does not induce TPC6A aggregation"*) appears **in the Discussion with no figure**, attributed to prior work. The supporting aggregation experiments are **transient overexpression** of EGFP/ECFP/EYFP fusions in COS7, SCC-9, BCC, B16F10, HEK293. |
| 2 | TPC6AΔ → TIAF1 → tau/Aβ, sequential | **PARTIAL** | Immunostaining of plaques in `Wwox−/−` cortex and postmortem AD hippocampi supports co-occurrence and one ordering (TPC6A plaques then TIAF1). Sequence is inferred from knockdown experiments reported elsewhere, not shown here. |
| 3 | Aggregates → mitochondrial failure → apoptosis | **PARTIAL** | Real in the dish, overexpression-dependent throughout. CCCP and UV reproduce relocation. |
| 4 | WWOX binds TPC6AΔ via the **SDR/D3 tail** (aa 120–414), not the WW domains (aa 1–95) | **SUPPORTED** | FRET + domain mapping, reciprocal endogenous co-IP in HEK293. This is the paper's most solid result and the one with SDR relevance. |
| 5 | WWOX accelerates TPC6A nucleolus↔mitochondrion shuttling | **SUPPORTED (single experiment)** | The **only genotype-controlled experiment in the paper**: `Wwox+/+` MEF 20 min round trip vs `Wwox−/−` 40–60 min. Kinetics in fibroblasts, not neurons. |
| 6 | WWOX loss → GSK3β activation → tau hyperphosphorylation | **SUPPORTED, three sources, now with a site conflict** | See § C. |
| 7 | WWOX → lysosomal proteostasis | **CONTRADICTED as stated in the batch brief** | `41677633` shows WWOX **routes other proteins** (Bcl-XL, Mcl-1) to the lysosome. `CMA`, `chaperone-mediated`, `LAMP`, `HSC70`, `HSPA8` occur **zero times** in the deposit; so do `WWOX degradation` and `half-life`. See § H. |
| 8 | Aggregation cascade → neuronal dysfunction | **PARTIAL** | Supported behaviourally in `Wwox+/−` mice (§ H), all at 10–11 months — an **ageing** phenotype, not a developmental one. |
| 9 | pY33/pS14 phospho-switch as the governing node | **UNKNOWN — and internally contradicted** | See § G-2. |

**Two load-bearing steps in `27551439` rest on `(Chen, unpublished)`**: the intramolecular WW–SDR
folding, and the TGF-β/Hyal-2/WWOX/Smad4 route to neuronal death. Same pattern `PAPER 088` already
carries. *(Note the first one is independently substantiated: `D-04` already records WW2 capping the
WW1 groove, from the structural literature. Chang's unpublished claim happens to be right — which is
a reason to source it properly, not a reason to accept it on his citation.)*

---

## B · Therapeutic intervention table — the `Requires WWOX?` column is the batch's answer

| Intervention | Target / node | **Requires WWOX?** | Model | Dose / exposure | Rescue endpoint | WOREE transferability | Evidence |
|---|---|---|---|---|---|---|---|
| **LiCl** | GSK3β (global) | **No — and that is the problem** | `Wwox−/−` mouse, PTZ | i.p., single | PTZ seizure suppression | **LOW** — suppressed in **all three genotypes incl. WT** | `PAPER 019`, image locator |
| **Zfra1-31 / Zfra4-10 — "zfration" arm** | covalent cross-link of Ser-containing peptides → proteolysis | **NO — cell-free chemistry** | PBS, synthetic peptides, recombinant His-Tau, cell lysates | 100 µM in vitro | blocks Aβ42, TPC6AΔ, WWOX7-21 aggregation; MG-132 does not block; no ubiquitin | **the one arm that could work in a WWOX-null brain** | `29067327` §3.6–3.7 |
| **Zfra4-10 — in vivo arm** | Hyal-2/WWOX/Smad4 → Z cells | **YES** | 3×Tg-AD, melanoma-bearing nude mice | 2 mM ×100 µL tail vein, weekly ×4 | memory restored; pS14-WWOX ↓87 % | **LOW** — every in vivo model has **intact WWOX**; never tested in `Wwox−/−` | `29067327`, `36498839` |
| **pY33-WWOX peptide (aa 28–38, KDGWVpYYANHT)** | decoy for endogenous pY33-WWOX | **YES — explicitly** | MPP⁺ rat brain | intracerebral | blocks MPP⁺ neuronal death; non-phospho peptide inert | **LOW** | `18371080`; mechanism stated in `36498839` Discussion |
| **WWOX7-21 / WWOX7-11** | endogenous WWOX phospho-state, IκBα/WWOX/ERK | **YES** | melanoma, skin cancer, 4T1 spheres | synthetic peptide | cancer growth/metastasis ↓ | **LOW** — no neuronal, no LoF endpoint | `31752354` (abstract) |
| **pS14-WWOX7-21** | same peptide, phosphorylated | YES | mouse xenograft | — | **cancer growth ↑↑** | ⚠️ **safety** — one phospho-state **inverts the sign** | `31752354` (abstract) |
| **WWOX286-299 / pY287** | surface epitope | YES | — | — | — | LOW | `31752354`, `34140629` (unread) |
| **SP600125 (JNK-i), PD-98059 (MEK-i)** | JNK1 / ERK | acts downstream of WWOX loss | WOX1-knockdown SK-N-SH | in vitro | **blocks tau phosphorylation and NFT formation in WWOX-deficient cells** | **the most interesting unexplored entry in this table** | `15126504` (abstract) |
| **Chloroquine** | lysosome | n/a — tool | `Wwox−/−` MEF | — | blocks Bcl-XL/Mcl-1 loss | none — wrong substrate | `41677633` |
| **NAC (antioxidant)** | ROS → WWOX induction | n/a | MEF | — | **reduces WWOX induction** | ⚠️ **counter-directional** for a LoF genotype | `41677633` |

🔴 **The decisive experimental gap of this entire corpus:** the Chang lab owns `Wwox−/−` mice and
`Wwox+/−` mice and uses them in these very papers — **and has never tested Zfra, or any of its
peptides, in a WWOX-deficient animal.** Every efficacy demonstration is in a WWOX-intact model.

---

## C · LITHIUM — **DOWNGRADE**

**The third source arrived and it strengthens the mechanism while weakening the drug.**

`PMID 15126504` (`FT-024`, Sze/Chang 2004) — **abstract only; the full text remains unobtainable**
(no PMCID; NCBI and Europe PMC both policy-denied here). `FT-024` stays **OPEN**.

| Evidence | Model | WWOX dependence | Intervention | Rescue | WOREE transferability |
|---|---|---|---|---|---|
| Sze 2004 (`15126504`) | SK-N-SH, WOX1 siRNA; AD hippocampi | direct — WWOX knockdown is the manipulation | **SP600125, PD-98059** | **yes — tau-P and NFT blocked** | mechanism T2; intervention untested in vivo |
| Wang/Lu 2012 (`22193544`, `PAPER 056`) | SH-SY5Y, recombinant, mouse-brain co-IP | residue-mapped (SDR 388–407 / L404) | none | n/a | T2, no allele tested |
| Cheng/Hsu 2020 (`32000863`, `PAPER 019`) | `Wwox−/−` mouse, PTZ | genotype | **LiCl** | **yes — but in WT, het and KO alike** | **LOW** |

**Why DOWNGRADE and not KEEP:**

1. The known negative **stands and is now sharper**: LiCl suppressed PTZ seizures in all three
   genotypes. It is an anticonvulsant working in a model that seizes.
2. **Sze 2004 had the opportunity to test a GSK3β inhibitor and did not.** It reports GSK-3β
   activation on WWOX knockdown, then rescues with **JNK and MEK inhibitors instead**. Across the
   entire three-paper field, **no one has ever shown that inhibiting GSK3β corrects a WWOX-loss
   phenotype.** The lithium rationale has been inherited, never tested.
3. ⚠️ **New site conflict, unresolved.** Sze 2004 reports *"enhanced phosphorylation of GSK-3β"* on
   WWOX knockdown; Wang 2012 reports GSK3β total **and phospho-S9 unchanged** while kinase output
   falls. `CLAIM 035` already warns that a pS9 readout produces a **false negative** here. **The
   Sze 2004 abstract does not name the site** — and the full text would settle it. This is now the
   single most valuable unread sentence in the lithium line.

**What survives:** the *mechanism* (arc 6) gets its third source and is stronger than before. The
*drug* does not. → `TX-005` **DOWN**. Not dismissed: `FT-022` (GSK-3β2 isoform, paywalled) remains
the live `REVIVAL_TRIGGER`, and **JNK/MEK inhibition is a better-evidenced lever than lithium on
this same axis and is currently nowhere in the portfolio.**

---

## D · ZFRA — **DOWNSTREAM TOOL**

Not "therapeutic candidate". Not "directionally incompatible" wholesale — that would be wrong, and
the audit found the arm that makes it wrong.

**Critical sign test, per activity:**

| Activity | Classification | Basis |
|---|---|---|
| "Zfration" — covalent cross-linking of Ser-containing peptides, ubiquitin/proteasome-independent proteolysis | **WWOX-INDEPENDENT / DOWNSTREAM** | demonstrated **cell-free in PBS** on synthetic Aβ42, TPC6AΔ peptides and recombinant His-Tau — **no WWOX in the tube** |
| Hyal-2/WWOX/Smad4 → Z-cell activation | **WWOX-DEPENDENT** | the lab's own stated mechanism; and Z cells *"did not appear to migrate to the brain"* |
| Suppression of pS14-WWOX (87 %) correlating with neuroprotection | **WWOX-DEPENDENT** | `29067327` §3.4 |
| "Zfra binds WWOX … accelerated WWOX degradation" | **WWOX-INHIBITORY** | `36498839`, `38542478` |

**Verdict.** The zfration chemistry is a genuine downstream anti-aggregation mechanism that does not
need WWOX, and it is worth keeping as a lead. The **therapeutic package is not**, for four reasons
that are all the authors' own:

1. **Never tested in WWOX deficiency**, though the lab has the mice (§ B).
2. **No established CNS route.** Zfra deposits in the spleen; Z cells do not reach the brain; the
   authors write they *"do not exclude the possibility"* that Zfra crosses the BBB and that Z cells
   *"conceivably"* secrete something that does. The route is unexplained by the people proposing it.
3. **The window closes with burden.** Treated at 10 months it works; *"when 3×Tg mice are at age 12
   months, injected Zfra fails to restore memory deficit."* WOREE is neonatal-onset and catastrophic.
4. **The lab's own model of benefit points the wrong way:** *"the stronger the binding of WWOX with
   intracellular protein partners, the better… By the same token, neurodegeneration is likely to be
   retarded when **WWOX has strong physical binding interactions** with protein partners."* That
   requires WWOX to be there.

Also: Zfra binds the **first WW domain** — N-terminal, not SDR. For SDR missense alleles the
WWOX-binding arm is in the wrong domain regardless.

*Context, not disqualifying:* US patent #10344065 on Zfra, and *"a clinical trial for Zfra has been
planned"*. Register the interest; weigh the data.

---

## E · Peptides other than Zfra

Assessed separately, as instructed — and they do **not** share Zfra's mechanism.

Against the operator's ladder for `31752354`: **epitope presence** — yes, but located on a
**simulated** 3-D structure, not an experimental one (the same defect class as `PAPER 056`'s GOR IV
model grafted onto 1O9U). **Extracellular accessibility** — supported by immunoelectron microscopy
and antibody access. **Function** — yes, in vivo, oncological. **Signalling** — claimed.
**Internalisation** — shown for the pY33-WWOX/Hyal-2 *complex*, not for the peptide.
**Therapeutic rescue in a LoF setting** — **none; never attempted.**

**"Surface epitope" does not reach "protein replacement route."** The gap is mechanistic, not
evidential: WWOX7-21 works by **modulating endogenous WWOX** (upregulating pY33-WWOX, disrupting
IκBα/WWOX/ERK). It is a modifier of a protein the reference genotype does not have.

⚠️ **The one durable finding here is a safety one**, and it generalises beyond this peptide:
`pS14-WWOX7-21` — the same 15-mer, one phosphate different — **increased cancer growth in vivo** and
protected cancer cells from apoptosis. Any WWOX-derived peptide therapeutic has a sign that depends
on a phospho-state the prescriber does not control.

---

## F · Missense / SDR assay value — **PARTIAL**

| Candidate readout | Domain | Useful for SDR alleles (Q230P class)? |
|---|---|---|
| **TPC6AΔ binding to the SDR/D3 tail** | SDR (aa 120–414, narrowed to D3) | **PARTIAL — the real candidate.** A second, orthogonal SDR-domain function beside `CLAIM 035`'s GSK3β pull-down. But mapped only by FRET on overexpressed fusions, no residue resolution, and **no missense allele has ever been tested.** |
| Tau binding via SDR | SDR | PARTIAL — and it **contradicts** the Wang 2012 negative (§ G-3) |
| pY33 / pS14 / pT12 / pY287 phospho-switch | **N-terminal WW1 region** | **NO for SDR alleles** — wrong domain. Relevant only to WW-domain variants. |

So: the Chang corpus **does** offer a candidate complementary SDR readout, and it is *not* the
phospho-switch the batch brief expected. Not promoted to a candidate: measurability, specificity and
causal relevance are not established, and `D-04` warns that an SDR readout which measures binding may
measure occlusion rather than function.

---

## G · Chang ↔ Aldaz, and Chang ↔ Chang — the five that matter

| # | Claim | Chang evidence | Counter-evidence | Model difference | Verdict |
|---|---|---|---|---|---|
| 1 | **WWOX is pro-apoptotic / mitochondrial-nuclear** | ubiquitous in `27551439`, `31752354`, `29067327` | Aldaz (`PAPER 053`): perinuclear/Golgi; pro-apoptotic role an **adenoviral-vector artefact** | **This wave makes the dispute legible: in `27551439` every apoptosis result is a transient-overexpression result.** The one endogenous experiment (co-IP) shows binding, not killing. | **Aldaz better supported on method.** Chang's apoptosis phenotype is not shown at endogenous stoichiometry anywhere in this wave. |
| 2 | **Zfra acts by blocking pY33-WWOX** | `29067327` **Introduction** asserts it | `29067327` **Results §3.4** measure **2 ± 6 % pY33 suppression** — i.e. none — and 87 ± 5 % pS14 suppression instead | none — same paper | 🔴 **Results win. The Introduction is wrong about its own paper**, and the 2024 review `38542478` propagates the Introduction's version. |
| 3 | **WWOX binds tau** | Sze 2004: binds via SDR. `36498839`: *"The SDR domain binds GSK3β and the C-terminal region of Tau"* | Wang 2012 Suppl. Fig. A, claimed to show *"WWOX does not associate with Tau"* | same lab lineage (Chang senior on both) | **`DIS-010` should move from NON STABILITA toward refuted.** The negative had no data behind it (`D-14`) **and** is contradicted twice by the same lab. ⚠️ Sze 2004's mapping involves yeast two-hybrid (MeSH confirms) — binding yes, *direct* binding not established. |
| 4 | **Y112 controls TPC6AΔ aggregation / relocation** | Results: Y112F *"had a reduced aggregation"*; Results name **Tyr112** for cytoplasmic relocation | Discussion: *"alteration of Tyr112 to Phe **does not reduce** TPC6AΔ aggregation"*; Discussion names **Tyr216** | none — same paper, two sections | 🔴 **Unresolved and self-contradictory.** Also: S35G *"failed to undergo aggregation"* then *"TGF-β1 significantly increased the aggregation of the S35G mutant"* two sentences later. |
| 5 | **Wwox haploinsufficiency is benign** | — | `29067327` §3.5 + `36498839` §2.5–2.7: `Wwox+/−` mice show **significant** memory deficits and cortical aggregates | Aldaz measured **lifespan and mammary morphology**; Chang measures **aged cognition** | **Not a contradiction — different endpoints.** See § H. |

---

## H · Therapeutic queue delta

| Node | Delta | Why |
|---|---|---|
| **`CLAIM 032`** — *haploinsufficiency is not deleterious; the therapeutic threshold is well below full restoration* | 🔴 **DOWN — counter-directional evidence, on the exact axis the claim declared untested** | `CLAIM 032` already carried its own caveat: *"la soglia è nota per **sopravvivenza e morfologia**, **non per cognizione ed epilessia**."* Two Chang-lab experiments now test cognition: `Wwox+/−` mice decline faster than 3×Tg-AD (`29067327` §3.5) and perform significantly worse than WT on short- and long-term ORT with cortical TPC6AΔ/SH3GLB2 aggregates (`36498839` §2.5–2.7, *"lacking one allele … leads to memory deficiency"*). **Caveats that must ride with it:** one laboratory (corroboration, not independent replication); 10–11-month **aged** mice, not development; §3.5 reported as a single sentence with no n and no statistic; figure panels not inspectable here; and every published human carrier parent remains clinically well. **This does not overturn `CLAIM 032` and must not be written as if it did** — it fires the claim's own implicit revival trigger and weakens the *"partial mosaicism may suffice"* corollary for long-term cognitive outcome specifically. |
| **`TX-005`** lithium / GSK3β | **DOWN** | § C. Mechanism up, drug down. No one has ever inhibited GSK3β against a WWOX-loss phenotype. |
| **`TX-003`** proteostasis / CMA | **UNCHANGED** | § A-7. `41677633` is about WWOX as a *router* of Bcl-XL/Mcl-1 to the lysosome. `CMA`/`LAMP`/`HSC70` appear **zero times**. The operator's caution was exactly right; no bridge exists. |
| **Protein replacement / extracellular WWOX** | **UNCHANGED** | § E. Surface epitopes are real; the peptides modulate endogenous WWOX and do not replace it. |
| **Downstream aggregation blockade** | 🆕 **NEW — lead, not candidate** | Zfration is a WWOX-independent, ubiquitin-independent anti-aggregation chemistry (§ D). Decisive experiment is cheap and has never been done: **Zfra in a `Wwox−/−` or `Wwox+/−` animal.** |
| **JNK / MEK inhibition** | 🆕 **NEW — lead** | `15126504`: SP600125 and PD-98059 block tau-P and NFT formation **in WWOX-deficient cells**. Better evidence of a WWOX-loss-specific pharmacological rescue than lithium has, and absent from the portfolio. Abstract-only; needs the full text. |
| **NAC / antioxidants** | ⚠️ **flag** | `41677633`: NAC *reduces* WWOX induction. Counter-directional in a genotype that needs more WWOX. |
| `CLAIM 016` / `CLAIM 035` | **UNCHANGED, mechanism corroborated** | Third source arrived; `36498839` restates Wang 2012 accurately (S396/S404). Status `in observation` stands — the site conflict (§ C-3) must be resolved first. |

**No new therapeutic candidate is created by this wave.** Two leads, one downgrade, one
counter-directional finding against a VERY HIGH-relevance claim, one safety flag.

---

## I · Scientific output

- **Processed:** 8. **Primary full-text (partial depth):** 5 — `27551439`, `29067327`, `36498839`,
  `41677633` (abstract + targeted Results), `26355344` (complete but it is a News piece).
  **Abstract-only:** 3 — `15126504`, `18371080`, `31752354`.
- **Reviews / non-primary identified:** 1 (`26355344`, mis-tiered as Tier B secondary evidence).
- **Deferred:** `34140629`, `32764489`, `22202011`, `25537520`, and the WW-domain/Hyal-2 arc.
- **Evidence gaps:** (a) `15126504` full text — names the GSK-3β phospho-site and settles § C-3;
  (b) `FT-022` still paywalled; (c) **Zfra in a WWOX-deficient animal — never done by anyone**;
  (d) no figure adjudication possible in this checkout.
- **Contradiction findings:** 4 internal to single Chang-lab papers (§ G-2, G-4 ×3), 1 cross-paper
  (§ G-3), 1 genre mis-tier (§ 0).
- **Dismissal movement proposed:** `DIS-010` → refuted (§ G-3).
- **Harness findings registered, not fixed** (per §13): `safe_push.py` has no `--help` handling and
  treats `--help` as a remote name, running the full gate and attempting a push; `reading_state.py`
  ignores `--out` and prints to stdout; network policy denies NCBI/EBI, which silently caps reading
  depth for every future wave in this environment.

---

## J · Saturation — **YES, continue**

Not saturated. The last two papers both moved the therapeutic queue (`CLAIM 032` counter-evidence)
and the contradiction map. But **Wave 2 should be re-scoped away from the batch's original plan**:
the aggregation-cascade arc is now well enough characterised that more of it will mostly restate
itself, while three specific questions are live and cheap —

1. `15126504` full text (author contact / ILL — the only route left) → settles the GSK3β site.
2. Has anyone, anywhere, put Zfra or a GSK3β inhibitor into a WWOX-deficient animal?
3. `34140629` (WWOX286-299, *Commun Biol*) — the one peptide paper in a journal outside the lab's
   usual venues, and the only one with an independent-seeming review process.

**Revised scope estimate: 8–12 more papers, not 19–23.** The corpus is large but its marginal
information is concentrated.

---

## K · Next scientist — not yet reassessed

Chang is not closed. Deferred to batch end, as instructed. One early signal: **Paula I. Moreira
(Coimbra, `35984507`)** is the only laboratory outside NCKU to have used a Zfra peptide, and used it
as *"the specific inhibitor of WWOX"* in a neuronal model — making her the natural independent
adjudicator of § D. That may matter more than the Richards/O'Keefe runner-up.

---

**STOP — Wave 1 closed. Awaiting operator direction on the revised Wave 2 scope.**
