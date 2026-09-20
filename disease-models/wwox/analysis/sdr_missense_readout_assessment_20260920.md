# Is there an experimental readout for WWOX SDR-domain missense alleles in the Chang/NCKU corpus?

**Batch:** `SCIENTIST_CHANG_NS_WWOX_NEUROPROTEOSTASIS_AND_PEPTIDE_INTERVENTION` · **Actor:** Scientist A
**Date:** 2026-09-20 · **Wave:** 3 (the last unresolved limb of the brief)
**Status:** non-canonical analysis file. No canonical file edited. No gate created. No receipt claimed
for a paper not already receipted, except as noted in § 0. **Not medical advice.**

> **The question, restated exactly.** Does the Chang/NCKU corpus provide an experimental readout
> usable on **WWOX missense variants of the SDR domain** — complementary to the one LEGEND already
> holds in `CLAIM 035` (GSK3β pull-down + Tau kinase inhibition, Wang/Lu 2012, PMID 22193544)?
>
> **Answer: `NO`.** Not "not yet", not "partially". The corpus contains eight candidate readouts.
> Every one of them is a **binding, localisation, conformation or dye** measurement. Not one is an
> assay of SDR *catalysis* or of a residue-mapped SDR *function*, and not one would distinguish a
> Q230P-class allele that is **present but inert** from a Q230P-class allele that is **absent** —
> which, per `DIS-003`, is the actual state of the reference genotype's own protein.

---

## 0 · Read depth, stated before any finding

| PMID | Short identity | Depth this wave | Figure access |
|---|---|---|---|
| **34140629** | Chen YA … Chang NS, *Commun Biol* 2021 — "Normal cells repel WWOX-negative or -dysfunctional cancer cells via WWOX cell surface epitope 286-299" | 🟢 **full PMC deposit read this wave** (61,298 B, cached `PMID34140629_PMC_MCPtext.txt`). Wave 1 listed it `(unread)`; it is now read. **Absent from the paper registry** — `registry_records.py get --pmid 34140629` returns no record. | ❌ none |
| 27551439 | Chang JY & Chang NS, *Cell Death Discov* 2015 — TPC6AΔ/TIAF1/tau/Aβ cascade | 🟢 full deposit (Wave 1 receipt) | ❌ none |
| 25650666 | Chang JY … Chang NS, *Oncotarget* 2015 — TRAPPC6AΔ extracellular plaques | 🟢 full deposit | ❌ none |
| 32764489 | Su WP … Chang NS, *Cancers* 2020 — Zfra4-10 / WWOX7-21 complex formation | 🟢 full deposit | ❌ none |
| 24932569 | Aldaz, Ferguson & Abba, *BBA Rev Cancer* 2014 — WWOX at the crossroads (**not Chang; read as the adjudication counterparty**) | 🟢 full deposit | ❌ none |
| 41677633 | Su YH … Chang NS, Hsu LJ, *Cells* 2026 — WWOX induction → Bcl-X_L/Mcl-1 lysosomal degradation | 🟢 full deposit | ❌ none |
| 29067327 · 31752354 · 36498839 · 26355344 | Zfra / peptide / commentary arm | 🟢 full deposits (Wave 1) | ❌ none |
| **22193544** | Wang HY … Lu PJ, *Cell Death Differ* 2012 — the incumbent | ⚪ **not re-read this wave.** Used at the depth `CLAIM 035` records, which LEGEND holds as a complete read. | — |
| **15126504** | Sze CI … Chang NS, *JBC* 2004 — WWOX–Tau binding via SDR | 🔴 **abstract only. No PMCID. Unobtainable in this environment.** See § 2.3. | ❌ |
| **29808465** | Johannsen et al., *Neurogenetics* 2018 — the Q230P source behind `DIS-003` | 🟡 **abstract only — no PMC deposit exists.** The load-bearing sentence is in the abstract and is quoted verbatim in § 3. | ❌ |

> 🔴 **Acquisition ceiling, inherited and re-confirmed.** `curl` → eutils/EBI returns 403; `WebFetch`
> → pmc.ncbi.nlm.nih.gov / jbc.org / sciencedirect.com returns `EGRESS_BLOCKED`; no PDF or figure
> tooling is present. The PubMed MCP text extraction additionally **strips figure callouts**, leaving
> bare `()`. **Consequence: not one finding below is anchored to a figure panel.** Where a paper's
> claim rests only on a panel, this file says so and does not adjudicate it (`D-14`).

---

## 1 · The assessment table

Four criteria, in order. **A readout fails if it fails any one.**

| Candidate readout | Source | 1 · Measurable? | 2 · Specific to SDR *function*? | 3 · Causally relevant? | 4 · Survives a destabilising missense? | Verdict |
|---|---|---|---|---|---|---|
| **GSK3β pull-down + Tau S396/S404 kinase inhibition** *(the incumbent, for comparison)* | PMID 22193544 via `CLAIM 035` | ✅ yes — recombinant protein, defined substrate, quantitative kinase output | ✅ yes — residue-mapped to 388–407, **L404 strictly necessary**; Axin-like docking motif | ✅ yes — Tau/microtubule assembly, neurite outgrowth; `S9`-independent | 🟡 **conditional** — in a *purified* format yes, **if** soluble folded yield is measured and activity normalised to it; in a *cell-expressed* format no | **still the only one** |
| **TPC6AΔ binding to the C-terminal tail** | PMID 27551439 | 🟡 semi-quantitative (FRETc on transiently overexpressed ECFP/EYFP fusions, COS7) | ❌ **no — and worse than Wave 1 recorded.** Binding narrows to the **D3 tail**, and the paper's own control shows *the SDR alone does not bind* | 🟡 partial — aggregation cascade is an **ageing/AD** endpoint, not a developmental one | ❌ no — needs high-level ectopic expression of both fusions | **FAIL (2, 4)** |
| **"SDR domain possesses an oxidoreductase activity"** — RedoxSensor Red CC-1 staining of stable EGFP-SDR transfectants | PMID 34140629 | ❌ **no** — a fluorescence dye. No substrate, no cofactor, no kinetics, no catalytic-triad mutant control anywhere in the deposit | ❌ no — CC-1 reports **cellular redox potential**, which has many determinants; nothing ties the signal to WWOX catalysis | ❌ no — endpoint is cancer-cell repellence / retrograde migration | ❌ no — requires a *stable* line overexpressing an isolated domain | **FAIL (1, 2, 3, 4)** |
| **`repl` (WWOX286-299) surface-epitope exposure / cell-repellence migration assay** | PMID 34140629 | 🟡 yes-ish — time-lapse migration velocity + distance, antibody IF | ❌ no — this is an **epitope-accessibility (conformation)** readout. It is precisely the occlusion measure `D-04` warns against | ❌ no — metastasis / invasion endpoint | ❌ no | **FAIL (2, 3, 4)** |
| **Intramolecular WW↔SDR FRET ("closed form")** | PMID 34140629 | ✅ yes — FRETc, Youvan's equation, both domains as separate fusions | ❌ no — **explicitly a folding readout.** `D-04`: occlusion is anti-function, so a *higher* signal may mean *less* function | ❌ no — no disease endpoint attached | ❌ no — both fusions must be expressed | **FAIL (2, 3, 4)** — but see § 4, it answers a *different* useful question |
| **Subcellular localisation — mitochondrial targeting, lipid-raft residence, Golgi/perinuclear** | PMID 34140629 (raft), PMID 24932569 (Golgi), multiple | ✅ yes — colocalisation scoring | ❌ **no — this is the criterion-2 archetype.** A destabilised protein mislocalises *by being degraded or misfolded*; the assay cannot separate that from loss of a targeting signal | ❌ no | ❌ no | **FAIL (2, 4)** |
| **WWOX–Tau binding via the SDR** | PMID 15126504 (unobtainable), restated in PMID 25650666 | ⚪ **cannot assess — paper unobtainable.** But the restating paper concedes the mechanism is unknown | ❌ no residue resolution anywhere in the corpus; a binding readout, same `D-04` problem | 🟡 in principle yes (Tau) | ❌ no | **CANNOT ASSESS → treat as FAIL** |
| **Zfra binding / "zfration"** | PMID 32764489, 29067327 | 🟡 co-IP, cell-free peptide chemistry | ❌ no — **and the lab states the functional significance is unknown** (§ 2.5). `zfration` itself is cell-free chemistry on Ser-containing peptides, not a WWOX readout at all | ❌ no — cancer suppression endpoint | ❌ no | **FAIL (2, 3, 4)** |
| **Protein stability / turnover panel** — cycloheximide chase, MG132, chloroquine, E64d + pepstatin A | PMID 41677633 | ✅ the *toolkit* is real and quantitative | — | — | — | **NOT A READOUT AS USED** — the panel is pointed at **Bcl-X_L and Mcl-1**, with WWOX as the *effector*. It has **never been pointed at WWOX itself.** See § 4 |
| **SDR catalytic-triad point mutants S281A / Y293F / K297A** | PMID 24932569, **"Aldaz laboratory unpublished observations"** | ⚪ unpublished — no data shown | ❌ readout used was **perinuclear localisation**, not activity | ❌ no | ❌ no | **FAIL** — but it amends a standing batch statement, see § 5 |

---

## 2 · The evidence, with verbatim quotes

### 2.1 · TPC6AΔ binding is weaker than Wave 1 recorded — it maps to D3, and the SDR alone does not bind

Wave 1 recorded this as the batch's best SDR-relevant candidate: *"WWOX binds TPC6AΔ via the SDR/D3
tail (aa 120–414), not the WW domains (aa 1–95)"*, verdict **SUPPORTED**. Reading the deposit for
this specific question narrows it further, in the wrong direction.

> *"To map the binding domain(s) in WWOX, the C-terminal SDR domain/D3 tail (aa #120–414), rather
> than the WW domains (aa #1–95), bound TPC6AΔ. To further narrow down the binding region, we
> determined that the C-terminal D3 tail physically bound TPC6AΔ."* — **PMID 27551439**

And the paper's own negative control:

> *"In an appropriate control, TGF-β1 did not induce the binding of TPC6AΔ with SDR only (), and no
> cell death occurred."* — **PMID 27551439**

🔴 **Read together, these two sentences say the binding determinant is the D3 tail, and that the SDR
body on its own is inert in this assay.** Q230 sits in the SDR body — `CLAIM 030` records it as
**relSASA 0.000, buried, 8.2 Å from the catalytic triad**. An assay whose determinant is a
C-terminal tail cannot report on a buried core residue except through gross misfolding, which is
criterion 2's exclusion. The corpus never gives D3's residue boundaries numerically in any deposit
read here, so even the geometry cannot be checked.

**Verdict: the candidate second readout that opened this wave does not survive the first criterion
it is tested on.**

### 2.2 · The new candidate — and why "the SDR has oxidoreductase activity" is a dye, not an assay

PMID 34140629 carries a results heading that reads, on its face, like exactly what the brief asks for:

> *"SDR domain possesses an oxidoreductase activity and repels visiting WWOXd cells"* — **PMID 34140629**

The evidence underneath it, in full:

> *"We established stable transfectants of MDA-MB-231 cells expressing EGFP-tagged SDR domain or EGFP
> only (). The extent of ectopic expression is shown (). **The ectopic SDR domain exhibited a strong
> redox activity (stained with CC-1; )**. Again, the ectopic SDR domain was localized in the lipid
> raft (). The SDR domain is Y287 phosphorylated ()."* — **PMID 34140629**

The reagent is identified in the Methods:

> *"RedoxSensor Red CC-1 stain from Molecular Probes/Invitrogen (Carlsbad, CA)."* — **PMID 34140629**

🔴 **This is a general cellular redox-potential dye read on a stable overexpressing line.** There is
no substrate, no NAD(P)H cofactor, no rate, no Km, no catalytic-triad mutant control, and no
figure-panel access to check the quantitation. The whole-cell control elsewhere in the same paper
shows the dye is exquisitely sensitive to **cell-to-cell context rather than to WWOX enzymology**:

> *"From a remote distance of 500 μm, knockout MEF cells dramatically increased the redox activity
> (>5-fold; stained by RedoxSensor Red CC-1) in the wild type cells ()."* — **PMID 34140629**

A dye that moves 5-fold in *wild-type* cells because a *neighbouring* cell lacks WWOX is not
reporting WWOX catalysis. **This is the corpus's most consequential overclaim for the brief's
question:** a heading asserts an enzymatic activity that the data underneath do not establish, and
if it were carried forward at face value it would look like the missing readout.

`CLAIM 035` already records the reason to be sceptical independently — the oxidoreductase route is
the one *"whose physiological substrate is unknown"*. Nothing in this corpus supplies one.

### 2.3 · WWOX–Tau via the SDR — unobtainable, and conceded to be mechanistically empty

PMID 15126504 has no PMCID and is unreachable here by any permitted route. But the Chang lab
restates its own result in a deposit that *is* readable, and the restatement is self-limiting:

> *"WWOX also binds Tau via its C-terminal SDR domain, whereas **how the binding regulates the
> hyperphosphorylation of tau is unknown.** The likely scenario is that WWOX may act as a chaperone,
> which stabilizes proteins from misfolding and being degraded by the ubiquitin/proteasome system."*
> — **PMID 25650666**

The second sentence is flagged as speculation by its own wording (*"the likely scenario"*), and it is
not a readout. So: the corpus asserts an SDR–Tau binding with **no residue resolution and no
mechanism**. Even if the 2004 paper were obtained, a binding-only result would run into `D-04` (a
binding readout may measure occlusion rather than function) and into criterion 4 unchanged.

**Parked as an acquisition task, not escalated.** Routes that remain: author contact, WWOX Foundation
institutional access, ILL.

### 2.4 · Localisation — the criterion-2 archetype, and the corpus knows it

PMID 34140629 adds a third localisation compartment to the two the Chang↔Aldaz adjudication already
had (Chang: mitochondrial targeting within the ADH domain; Aldaz: Golgi localisation requires an
intact SDR):

> *"By colocalization analysis, both C-terminal SDR domain and D3 tail were needed for the
> localization of WWOX in the lipid raft (). The N-terminal WW domain did not support localization of
> WWOX in the lipid raft ()."* — **PMID 34140629**

> *"WWOX localization in the lipid raft is via its C-terminal SDR domain and the D3 tail in binding
> Flotillin-2."* — **PMID 34140629**

All three compartments are mapped with **deletion constructs** — `EGFP-WW`, `EGFP-D3`,
`EGFP-ΔD3WWOX`, `EGFP-SDR`. The standing warning from the adjudication applies without modification:
**a deletion cannot separate "the SDR carries a targeting signal" from "an unfolded protein
mislocalises".** And a destabilising missense that is degraded scores identically to one that lost a
targeting signal. **Fails criterion 2 by construction, before criterion 4 is even reached.**

### 2.5 · Zfra — the brief's premise needs a correction, and the corrected version fails anyway

The brief states that Zfra binds WW1, the wrong domain. **That is incomplete.** The corpus says both:

> *"Zfra binds to WWOX at both the N-terminal WW domain and the C-terminal short-chain alcohol
> dehydrogenase/reductase (SDR) domain and suppresses WWOX phosphorylation at Tyr33 and its apoptotic
> function."* — **PMID 32764489**

So Zfra *does* engage the SDR. But the same paper, two sections later, removes any value this could
have as a readout — and does so about the SDR in general:

> *"WWOX utilizes its first WW domain at the N-terminus to bind PPXY motif-containing proteins. When
> Tyr33 is phosphorylated, WWOX has an expanded binding capability. In addition to the first WW
> domain, **the C-terminal SDR domain also binds to many proteins. Although the functional
> significance of the binding is unknown**, an enhanced binding of WWOX with its partners is critical
> in blocking cancer cell growth in vivo."* — **PMID 32764489**

🔴 **This single sentence is the corpus's own answer to the brief's question.** The lab that owns the
corpus states, in print, that the SDR is a promiscuous binding surface **whose functional
significance it does not know**. A readout built on a binding event of admittedly unknown functional
significance cannot satisfy criterion 2 or criterion 3, whichever allele it is run on.

### 2.6 · The stability toolkit exists in the corpus — pointed at the wrong protein

PMID 41677633 is the only paper in the corpus with a real protein-turnover methodology:

> *"Etoposide, cisplatin, hydrogen peroxide, doxycycline hyclate, chloroquine diphosphate salt,
> (2S,3S)-trans-epoxysuccinyl-L-leucylamido-3-methylbutane ethyl ester (E64d), MG132, cycloheximide,
> and N-acetyl-L-cysteine (NAC) were purchased from Sigma."* — **PMID 41677633**

> *"These results suggest that WWOX promotes Bcl-X_L and Mcl-1 protein degradation upon serum
> starvation through the lysosome/autophagy-mediated pathway."* — **PMID 41677633**

WWOX is the **effector** throughout; its own regulation in that paper is **transcriptional**
(*"stress responses … increase WWOX expression … through transcriptional activation"*). The words
`half-life`, `WWOX degradation`, `CMA`, `chaperone-mediated`, `LAMP`, `HSC70` and `HSPA8` occur
**zero times** across every deposit in this corpus (verified by census over all ten cached texts).

**So: the corpus contains the assay panel that criterion 4 actually requires, and has never turned it
on WWOX.** That is the most actionable negative in this file.

---

## 3 · Criterion 4, stated plainly — why it kills nine of nine

Every cell-based readout above requires the mutant protein to be **present, in the cell, at a level
sufficient to be detected.** For the reference genotype's own allele class, it is not:

> *"Functional studies showed **normal levels of WWOX transcripts but absence of WWOX protein.** … This
> could be explained by the functional data indicating an impaired translation or premature
> degradation of the WWOX protein."* — **PMID 29808465** (abstract; the source behind `DIS-003`)

`CLAIM 030` records the consequence across the allelic series: **Q230P (SDR) → protein absent →
severe; G372R (SDR) → protein barely detectable by IF → mild; P47T (WW1) → normal protein levels,
binding abolished → mild.** Protein abundance does not predict severity — but every assay in § 1
*measures something that scales with abundance*.

🔴 **Therefore, for a Q230P-class allele, every binding, localisation, conformation and dye readout in
this corpus returns the same number as a complete null — and that number is uninformative.** It
cannot distinguish "the allele has no SDR function" from "the allele was degraded before the assay
started". That distinction is the entire point of having a function readout. This is criterion 4, and
it is not a technical inconvenience: it is the reason the question was asked.

The incumbent `CLAIM 035` assay is the **only** candidate with a route around it, and only in one
specific format — **purified recombinant protein with soluble yield measured and activity normalised
to folded monomer**. Nobody has run it that way on any WWOX-DEE allele. `CLAIM 035` records the gap
itself: *"Solo WWOX wild-type e mutanti ingegnerizzati — **nessun allele WWOX-DEE è stato testato**."*

---

## 4 · Verdict

# `NO`

**The Chang/NCKU corpus provides no experimental readout usable on WWOX SDR-domain missense variants,
and therefore provides nothing complementary to `CLAIM 035`.**

The three sentences that carry the verdict, all from the corpus itself:

1. *"the C-terminal SDR domain also binds to many proteins. **Although the functional significance of
   the binding is unknown**"* (PMID 32764489) — the corpus disclaims function for its own binding
   readouts.
2. *"TGF-β1 did not induce the binding of TPC6AΔ with SDR only"* (PMID 27551439) — the one candidate
   second readout does not engage the SDR body.
3. *"The ectopic SDR domain exhibited a strong redox activity (stained with CC-1)"* (PMID 34140629) —
   the corpus's only claim of SDR *enzymatic* activity is a dye on an overexpressing line.

**Complementarity was the test, and it fails on both halves.** A complementary readout would have to
(a) report a different SDR function than GSK3β docking, and (b) be robust where the incumbent is
weak. The corpus offers nothing that does (a) — no substrate, no catalysis, no second mapped motif —
and nothing that does (b), since every candidate is *more* abundance-dependent than the incumbent,
not less.

**One honest qualification, recorded so it is not lost.** The intramolecular **WW↔SDR FRET** assay
(PMID 34140629) is a *good* assay — for a different question. It measures whether the protein adopts
the closed form, i.e. **whether the allele folds**. That is exactly the stratifying variable
criterion 4 needs, and § 5 uses it. It is not a function readout, and `D-04` forbids reading it as
one: in WWOX, a *higher* closed-form signal means *more* occlusion, and occlusion is anti-function.
Classifying it as a folding probe rather than a function readout is what keeps it useful.

**A readout is not a therapy.** Nothing in this file proposes an intervention, and nothing here
should be read as supporting one. The brief is explicit that measurability, specificity and causal
relevance must be established first; on this corpus, none of the three is.

---

## 5 · Corrections this wave owes to earlier waves

| Standing statement | Correction | Source |
|---|---|---|
| "Zfra binds WW1, wrong domain." | **Incomplete.** Zfra binds *both* WW1 and the SDR. The correct reason to reject it is not the domain — it is that the lab declares the SDR binding's functional significance unknown. | PMID 32764489 |
| "TPC6AΔ binding maps to the SDR/D3 tail (aa 120–414), narrowed to D3." | **Narrower still, and disqualifying.** The paper's own control shows **SDR-only does not bind**. The determinant is the D3 tail alone. | PMID 27551439 |
| "Neither Chang nor Aldaz has ever tested an SDR *missense* allele. Only large deletions and truncations." | **Amend, do not retract.** Aldaz reports **S281A, Y293F and K297A** — genuine SDR point mutants — but ⚠️ as *"Aldaz laboratory unpublished observations"* in a review, with **no data shown**, and with **localisation** as the readout, not activity. These are also **catalytic-triad** mutants, not *destabilising* ones, so they do not test the disease-relevant allele class. The statement should read: *no published experiment has tested a destabilising SDR missense allele; one unpublished catalytic-site mutant series exists, read out by localisation.* | PMID 24932569 |
| PMID 34140629 listed `(unread)` and absent from the paper registry. | **Read in full this wave.** It is a *Commun Biol* primary with 31 SDR mentions — the single most SDR-dense deposit in the corpus. Registry entry missing; flagged, not created (read-only actor). | this file § 0 |

Verbatim, for the Aldaz correction:

> *"Furthermore, we generated GFP-WWOX proteins containing single point mutations (S281A, Y293F, and
> K297A) destroying WWOX's catalytic activity. Remarkably, we observed that the amino acids predicted
> to be required for WWOX enzymatic activity were also necessary for perinuclear localization
> **(Aldaz laboratory unpublished observations)**."* — **PMID 24932569**

---

## 6 · What would actually be needed

The corpus does not contain this assay. Concretely, a Q230P-class allele requires a **folding-normalised,
purified-protein function assay with an explicit degradation arm**. Five components, in dependency order.

**(A) Establish whether the allele exists as folded protein at all — before any function assay.**
This is prerequisite, not preliminary. Express full-length WWOX and the isolated SDR, wild-type and
mutant, in a heterologous system (E. coli with a solubility tag, or insect/mammalian if the SDR needs
eukaryotic folding), and report three numbers per allele that nobody currently reports: **soluble
yield per litre**, **thermal midpoint (nanoDSF `T_m`, or CD)**, and **monomer fraction (SEC-MALS)**.
An allele that yields no folded monomer is not "inert" — it is absent, and must be said so, not
scored as a negative.

**(B) Run the incumbent assay on that material, normalised per mole of folded monomer — not per mole
of plasmid.** The `CLAIM 035` assay (GSK3β pull-down + inhibition of Tau S396/S404 phosphorylation
*in vitro*) is the only SDR-function readout in existence. Normalising it to (A) is what converts it
from an abundance-confounded measurement into a function measurement. Controls that must be in the
same run:
- **P282A** — the `D-04` occlusion control: stable and completely inert. It is the assay's internal
  check that a binding signal is not being read as function.
- **G372R** — `CLAIM 030`'s natural mild-phenotype SDR control. If G372R and Q230P behave identically
  on normalised activity, the structural model is wrong and the readout is not stratifying.
- **L404A** — the positive-control loss-of-docking allele from `CLAIM 035` itself.
- ⚠️ **Never pS9 as a GSK3β activity readout.** `CLAIM 035` records that WWOX inhibition is
  S9-independent; a pS9 western on this system yields a **false negative**.

**(C) A degradation arm, because criterion 4 is two questions, not one.** In an isogenic cell system
expressing the mutant, ask whether *any* folded protein can be recovered: proteasome inhibition
(MG132), lysosome/autophagy inhibition (chloroquine; E64d + pepstatin A), cycloheximide chase for
half-life, and **low-temperature rescue (30 °C incubation)** — the classic discriminator between a
folding defect and a synthesis defect. 🔵 **This panel already exists intact in the corpus
(PMID 41677633) and has never been pointed at WWOX.** Running it as published, with WWOX as the
analyte instead of Bcl-X_L and Mcl-1, is the single cheapest missing experiment identified by this
assessment.

**(D) Replace the western-blot detection floor with absolute quantification.** The "protein absent"
call in PMID 29808465 is a western blot at its detection limit, and `CLAIM 030` already flags that the
abundance measurements across the allelic series (**WB on fibroblasts for P47T and Q230P; IF on
organoids for G372R**) are **not commensurable**. Targeted mass spectrometry (PRM/SRM) with a heavy
internal standard peptide from a tryptic region **unaffected by the variant** gives an absolute
copy number and a real lower bound. "Absent" and "below 2% of wild-type" are different findings with
different consequences, and the corpus cannot currently tell them apart.

**(E) The context the assay ultimately has to run in.** An isogenic knock-in of the missense allele in
an iPSC line, differentiated to cortical neurons, reading the GSK3β/Tau axis on **S396/S404** with
(A)-style protein quantification alongside. This is the only design in which criteria 3 and 4 are
satisfied simultaneously: a disease-relevant cell type, a disease-relevant endpoint, and an allele
present at its physiological expression level rather than an overexpressed fusion.

**And the gap that (A)–(E) do not close.** There is still **no substrate for the SDR's putative
oxidoreductase activity** — `CLAIM 035` records it, and nothing in this corpus supplies one. Until
one exists, "SDR function" can only ever be proxied by the GSK3β docking interaction, and
PMID 34140629's `CC-1` result must not be promoted into that gap. Identifying a physiological
substrate is the experiment that would make a genuinely *complementary* second readout possible. It
is not in this corpus, and on the census run here it is not anywhere.

---

*Non-canonical. Read-only toward all canonical files. No commit. Not medical advice.*
*Source attribution: article metadata and full texts retrieved from **PubMed / PubMed Central**.
DOIs — [22193544](https://doi.org/10.1038/cdd.2011.188) · [24932569](https://doi.org/10.1016/j.bbcan.2014.06.001) ·
[25650666](https://doi.org/10.18632/oncotarget.2876) · [26355344](https://doi.org/10.1038/cddis.2015.251) ·
[27551439](https://doi.org/10.1038/cddiscovery.2015.3) · [29067327](https://doi.org/10.1016/j.trci.2017.02.001) ·
[29808465](https://doi.org/10.1007/s10048-018-0549-5) · [31752354](https://doi.org/10.3390/cancers11111818) ·
[32764489](https://doi.org/10.3390/cancers12082189) · [34140629](https://doi.org/10.1038/s42003-021-02271-2) ·
[36498839](https://doi.org/10.3390/ijms232314510) · [41677633](https://doi.org/10.3390/cells15030270).*
