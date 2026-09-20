# Blunt-instrument audit of the canonical claims — which negatives rest on endpoints that could not have seen the phenotype

**Date:** 2026-09-20 · **Actor:** Scientist A ·
**Batch context:** generalisation of `SCIENTIST_CHANG_NS_WWOX_NEUROPROTEOSTASIS_AND_PEPTIDE_INTERVENTION`
· **File class:** non-canonical analysis.

> 🔴 **Read-only. No canonical file was touched.** Nothing under
> `disease-models/wwox/registries/`, `disease-models/wwox/therapeutics/` or `framework/` was edited,
> no commit candidate was created, no claim text, status or tag was changed, and nothing was
> committed. This file establishes an **evidence state**, not a repair.
> `fulltext_receipts.py verify` at the time of writing → **OK: 167 chained receipt(s), tail anchored**.

---

## 0 · The proposition being screened for

> **An apparently normal phenotype under a coarse endpoint becomes abnormal under a sensitive one.**

Three instances closed in the Chang/NCKU batch, in three unrelated questions:

| Instance | Coarse endpoint → verdict | Sensitive endpoint → verdict |
|---|---|---|
| `Wwox+/−` mouse, 3 weeks | rotarod, footprint/gait, limb-clasping → *"no significant differences"* | Tc-MEP latency **2.13 ± 0.22 ms (n=5) vs 1.39 ± 0.13 (n=10), p < 0.05** (amplitude normal); and, from an independent lab, spontaneous neocortical bursting in **4/23 het slices vs 0/11 WT** |
| `Wwox`-null (`lde`) cortex | bulk NeuN density and NeuN expression → *"**Wwox is not required for proliferation and migration of immature neurons**"* (PMID 31340538, Discussion) | Satb2/Tbr1 layer markers + E16.5 BrdU birth-dating, **same investigators, one year later** → *"**Wwox deficiency impairs prenatal neuronal migration**"* (PMID 32581702, Results). **Neuron number normal; laminar placement not.** |
| `CLAIM 032` | spontaneous neoplasia, lifespan, western-blot band intensity, gross observed behaviour → *"not deleterious"* | none applied — the neurological endpoints were never run on a heterozygote by the labs that own the claim's sources |

---

## 1 · Method — surfaces read and how

| Surface | Records | How it was read |
|---|---|---|
| `claim_registry_current.md` | **39** (CLAIM 001–039) | **read whole, in-file**, sequentially, every field of every record |
| `working_model_current.md` | **13** | read whole (Disease identity → BLOCK 3 → Monitoring endpoints), plus the BLOCK 2 claim mirror row by row |
| `dismissal_ledger_current.md` | 4 active | read for the negatives institution (`PREMISE_TAG`, `REVIVAL_TRIGGER`, `DEFAULTS THAT BIT US`) — used as a **control**, not as a target |
| `CC-20260920-CLAIM032-ENDPOINT-QUALIFIER-01` | 1 | read in full as the standing worked example |
| `wwox_heterozygote_phenotype_audit_20260920.md`, `wwox_developmental_timing_audit_20260920.md` | — | read for the batch's verbatim endpoint anchors |

Surface inventory and field vocabulary taken from `registry_records.py index` and
`registry_records.py fields` before any reading. 🔴 **`paper_registry_current.md` (457 records) and
`literature_tracking_log_current.md` (419) were never grepped and never opened** — every paper-level
fact below is quoted from inside a claim record, from the working model, or from the two batch
audit files, each of which carries its own receipt.

**Screen applied.** A record enters the table if it asserts, in its own words, some form of *normal*,
*not deleterious*, *no phenotype*, *no difference*, *indistinguishable*, *unaffected*, *absent*, or
*not required*. **19 of the 39 claims** carry at least one such assertion, plus the working model's
BLOCK 2 mirror. Positive claims carrying no negative assertion were screened and excluded, and are
not listed.

**Verdicts.** `SOUND` — endpoint matched the claim · `OVERSTATED` — endpoint cannot support the
scope claimed · `BLIND` — endpoint incapable of seeing the phenotype at all · `CANNOT ASSESS` — the
claim does not state its endpoint. Where one claim rests several negatives on different
instruments, each gets its own chain and its own verdict.

---

## 2 · The audit table

### 2.1 · `BLIND` — the endpoint could not have seen the phenotype

---

**`CLAIM 032` (leg A — Aldaz 2014) — WORKED EXAMPLE, covered by a standing candidate; nothing further is proposed for it here.**

- **CLAIM →** *"La perdita di **un solo** allele di WWOX non produce fenotipo"*; *"loss of one Wwox
  allele (i.e. **haploinsufficiency**) appears **not to be deleterious**"*; *"the lifespan of the
  Wwox heterozygotes was **indistinguishable from WT mice**"*. `clinical relevance: VERY HIGH`.
- **ENDPOINT USED →** spontaneous neoplasia across tissues, plus lifespan, observed over the animals'
  lifetime — in a **narrative review**, not a primary phenotyping study. The quoted sentence's
  subject is the preceding clause, *"no evidence of spontaneous neoplasia in any tissue examined"*,
  and the source continues *"…not to be deleterious **or carcinogenic**"*.
- **WHAT IT CAN ACTUALLY EXCLUDE →** that a heterozygote develops visible spontaneous tumours, and
  that it dies earlier than wild type. Nothing else. No cognitive, electrographic, motor-conduction
  or laminar endpoint exists in the source.
- **MORE SENSITIVE EVIDENCE →** Breton 2021 (Carlen, Toronto — outside the source lab): bursting in
  **4/23 Syn1-Cre het slices vs 0/11 WT**, *"may be reflective of epileptic network activity;
  however, there are no clear behavioral seizures"* — **no statistic reported**, het elsewhere
  pooled into `S-CTL`. Cheng 2020: het Tc-MEP latency `p < 0.05` at 3 weeks with rotarod/gait/
  clasping normal. Chang 2017 §3.5 / Chang 2022 §2.5: aged het memory decline — **single lab, no n**.
- **VERDICT → `BLIND`.** A tumour-and-lifespan endpoint is incapable of seeing a network or
  conduction phenotype. The claim's own caveat (*"la soglia è nota per sopravvivenza e morfologia,
  non per cognizione ed epilessia"*) is exactly right; `CC-20260920-CLAIM032-ENDPOINT-QUALIFIER-01`
  already proposes the qualifier. **No further proposal is made here.**

---

**`CLAIM 032` (leg B — Tochigi 2019)**

- **CLAIM →** *"i ratti **`+/lde`** hanno «a single band of normal molecular weight, but its
  intensity was **almost half**», con immunoistochimica corticale intensa come i `+/+`"*, carried in
  support of *"non produce fenotipo"*.
- **ENDPOINT USED →** western-blot band intensity and immunohistochemistry, at PND 5/10/15/21.
  **No behavioural, EEG, cognitive or electrophysiological test exists anywhere in that paper**, and
  its Methods **pool `+/+` with `+/lde` as "normal" controls**.
- **WHAT IT CAN ACTUALLY EXCLUDE →** that the het lacks WWOX protein, and that cortical layer V /
  corpus callosum immunoreactivity is grossly reduced. It is a **protein-dosage datum**, not a
  phenotype observation.
- **MORE SENSITIVE EVIDENCE →** none in this animal. The same rat line's het arm has never been run
  on EEG, on audiogenic-seizure susceptibility (`+/lde` is not mentioned in the Suzuki 2009
  abstract; body acquisition-blocked), or on a quantitative motor test.
- **VERDICT → `BLIND`.** This is priority-6 in its purest form: a protein-abundance readout standing
  in for function, in a design that structurally **cannot** report a het phenotype because the het is
  a control-group member. Covered by the standing candidate.

---

**`CLAIM 039` — *"…and it is not cerebellar"***

- **CLAIM →** title: *"Ataxic gait is the most penetrant phenotype of the rat `lde/lde` model — 95%
  versus 0% — **and it is not cerebellar**"*. Summary: *"Gli autori esaminano il cervelletto e **non
  trovano alterazioni patologiche marcate**, in contrasto esplicito con il topo *ataxia and male
  sterility* (AMS)."* `Status: in observation`.
- **ENDPOINT USED →** declared in the claim's own evidence boundary: *"il cervelletto è
  istologicamente indenne e nessun'altra regione, oltre a ippocampo e amigdala, mostra alterazioni
  **al microscopio ottico**"*, with the gait assessment itself *"osservazionale e non in cieco"* and
  *"non sono stati eseguiti test motori quantitativi (rotarod, footprint, analisi cinematica)"*.
- **WHAT IT CAN ACTUALLY EXCLUDE →** gross cerebellar histopathology visible by light microscopy —
  frank atrophy, layer loss, obvious vacuolation. It **cannot** exclude a cerebellar contribution:
  Purkinje-cell electrophysiology, climbing-fibre refinement, calbindin/Purkinje stereology,
  molecular-layer synaptic density and cerebellar output timing are all invisible to it. This is
  structurally the **NeuN instance**: the cells are there and are counted; how they are wired is not
  measured.
- **MORE SENSITIVE EVIDENCE →** **none in the corpus, in either direction.** No cerebellar
  electrophysiology, no Purkinje counts, no DTI and no quantitative gait analysis exists for the
  `lde` rat. Note the asymmetry the corpus already contains: the instrument that **did** find a
  motor abnormality where behaviour was normal — Tc-MEP latency, Cheng 2020 — has never been applied
  to this model. Note also the working model's own standing instruction, BLOCK 1 §4: *"avoid
  automatic cerebellar extrapolations"* — the claim's negative runs in the opposite direction from
  that caution and is not flagged as doing so.
- **VERDICT → `BLIND`.** The claim's **title asserts a mechanistic exclusion** (`not cerebellar`) on
  a light-microscopy endpoint incapable of testing it. The 95%-vs-0% penetrance half is `SOUND`; the
  negative half is not. 🔴 **The working-model BLOCK 2 mirror row 039 reproduces the exclusion
  verbatim, with no endpoint and no evidence boundary attached.**

---

**`CLAIM 013` (leg A — the MRI null)**

- **CLAIM →** *"Drug resistance, feeding, **MRI**, disabilità globale: **non differiscono
  significativamente tra genotipi**."* `clinical relevance: HIGH`.
- **ENDPOINT USED →** conventional MRI as a cohort-level categorical variable in a **parental-registry
  survey** of 50 biallelic individuals, FDR-corrected (Benjamini–Hochberg) across all tested
  associations. The claim declares the ascertainment (*"survey parentale con bias di sopravvivenza"*)
  but **not** the acquisition protocol, the sequence set, the field strength, or whether any central
  radiological review took place.
- **WHAT IT CAN ACTUALLY EXCLUDE →** a large, categorically-scored, conventional-MRI difference
  between genotype classes, surviving FDR at n≈50 split three ways.
- **MORE SENSITIVE EVIDENCE →** 🔴 **the model already holds the instrument's insensitivity as
  canon.** `CLAIM 012` (`consolidated baseline`): *"MRI normale in fase precoce **non esclude**
  disfunzione di rete severa. **Rafforza EEG come endpoint più sensibile dell'imaging** nelle fasi
  iniziali in WWOX-DEE."* `CLAIM 015` adds *"explains why early MRI may **underestimate structural
  burden**"*, and `CLAIM 002` shows the same blindness at cellular scale: organoid **size** is a clean
  null while **layer-marker placement** is not.
- **VERDICT → `BLIND`.** A null on an instrument this registry has already ruled insensitive to the
  phenotype in question is not evidence of no difference. The claim reports it in a list of
  non-significant associations without the `CLAIM 012` cross-reference that would defuse it.

---

### 2.2 · `OVERSTATED` — the endpoint cannot support the scope claimed

---

**`CLAIM 013` (leg B — drug resistance, feeding, global disability)**

- **CLAIM →** the same sentence: those three variables *"non differiscono significativamente tra
  genotipi"*.
- **ENDPOINT USED →** parent-reported categorical items in the same registry survey, FDR-corrected,
  n=50 across three genotype classes (so cells of roughly 10–25).
- **WHAT IT CAN ACTUALLY EXCLUDE →** a **large** difference on **coarse, parent-scored, global**
  descriptors. It cannot exclude a graded difference, and it cannot exclude any difference on the
  instruments that actually resolve this disease — EEG organisation, quantitative development
  scales, respiratory polygraphy.
- **MORE SENSITIVE EVIDENCE →** none applied in the source. Note that the **three associations that
  did survive FDR** — hypertonia, seizures, respiratory complications — are the three with the
  crispest parent-observable definitions, which is what one expects when the instrument, not the
  biology, sets the resolution.
- **VERDICT → `OVERSTATED`.** The claim's wording (*"non differiscono significativamente"*) is
  literally correct and is the right phrase; what is missing is that **an FDR-corrected null on a
  parental survey is a floor, not a negative** — the same distinction `CLAIM 037` already draws for
  the `lde` seizure rate (*"il 34% spontaneo è **un pavimento, non un tasso**"*).

---

**`CLAIM 030` (leg A — *"Q230P ha proteina assente"*) — the sharpest internal drift found**

- **CLAIM →** `CLAIM 030`, `clinical relevance: VERY HIGH`: *"**Q230P** (SDR) ha **proteina
  assente** → **severo**."*
- **ENDPOINT USED →** western blot on patient fibroblasts. The endpoint is stated correctly **one
  claim away**, in `CLAIM 019`: *"qRT-PCR → livelli di trascritto WWOX **normali**; **Western blot →
  proteina WWOX non rilevata**"*, and `CLAIM 019` then says explicitly *"Il DATO è quindi l'endpoint
  `mRNA normale + proteina non rilevata`, **non un meccanismo post-traduzionale**"*.
- **WHAT IT CAN ACTUALLY EXCLUDE →** WWOX immunoreactivity **above that blot's detection floor**, for
  **that antibody's epitope**, in **that cell type**. It cannot establish absence. A misfolded
  variant retaining 2–5% of wild-type abundance is indistinguishable from zero on a blot and is not
  indistinguishable from zero biologically — which matters precisely because `CLAIM 032` argues the
  functional threshold sits **below 50%**, and the `Wwox^gt/gt` hypomorph (*"proteina bassa **ma
  rilevabile**"*) is **viable** where the null dies.
- **MORE SENSITIVE EVIDENCE →** none run. Two routes exist and the registry names both: targeted
  mass spectrometry, and — better — `CLAIM 035`'s functional readout, *"pull-down GSK3β + inibizione
  della chinasi su Tau in vitro"*, proposed there as *"un saggio funzionale per gli alleli missense
  del dominio SDR"*. `RC-013` is the standing wet-lab candidate.
- **VERDICT → `OVERSTATED`.** 🔴 **Three formulations of the same datum coexist in canon and one is
  the outlier:** `CLAIM 019` — *"proteina non rilevata"*; working model BLOCK 1 INFERENCE — *"normal
  transcript with **protein not detected**; … residual function cannot be inferred from abundance
  alone"*; `CLAIM 030` — *"proteina **assente**"*. The registry's most careful claim about the
  abundance/function distinction is the one that converts a detection limit into an absolute. The
  load it carries is real: *"se Q230P non produce proteina, the reference genotype … potrebbe essere
  **funzionalmente null/null**"* (`CLAIM 019`, prognostic limb).

---

**`CLAIM 030` (leg B — *"G372R … organoidi forebrain quasi normali"*)**

- **CLAIM →** *"**G372R** (SDR) ha proteina quasi non rilevabile all'IF → **lieve**, con **organoidi
  forebrain quasi normali**."*
- **ENDPOINT USED →** immunofluorescence for abundance, and an **unspecified organoid endpoint** for
  *"quasi normali"*. The claim declares the abundance instruments and their incommensurability
  (*"WB su fibroblasti per P47T e Q230P; IF su organoidi per G372R. La serie orienta, **non
  quantifica**"*) but **never says what "quasi normali" was measured on** — size, gross morphology,
  layer markers, firing rate, or an author's summary sentence.
- **WHAT IT CAN ACTUALLY EXCLUDE →** depends entirely on which it was, and the corpus shows the
  spread is decisive: on the **same platform**, `CLAIM 002` records that organoid **size** is a clean
  null at every timepoint (wk6 `0,3675` … wk18 `0,8952`) — *"the model does not reproduce the
  microcephaly seen in some patients"* — while **layer-marker placement is not normal** and the AAV
  rescue is *"marker-selective, not uniformly normalising"*. A morphologically near-normal organoid
  is exactly what a WWOX-KO organoid looks like on the coarse axis.
- **MORE SENSITIVE EVIDENCE →** the `CLAIM 002` reading itself supplies the sensitive panel
  (CTIP2 / TBR1 / SATB2 laminar quantification, firing rate with `P = 0.7681`). Whether G372R
  organoids were ever run on it is not recorded.
- **VERDICT → `OVERSTATED`.** The human severity call (*"lieve"*) carries this limb; the organoid
  limb, on the endpoint most likely used, cannot. This is the **NeuN instance at organoid scale** and
  it sits inside the very claim whose thesis is that coarse abundance does not report function.

---

**Working model — BLOCK 2 mirror, rows 032 / 037 / 039**

- **CLAIM →** row 032: *"**Haploinsufficiency is not deleterious**: the therapeutic threshold sits
  well below full restoration"*. Row 037: *"…and is **explicitly absent** in Wwox-null mice"*.
  Row 039: *"…**and it is not cerebellar**"*. Plus the cross-cutting note: *"CLAIM 031 + CLAIM 032
  together state that … those levers **need not restore 100 %** of function. The portfolio narrows
  and **the threshold drops**."*
- **ENDPOINT USED →** **none is carried into the mirror.** The mirror's columns are Type, Pathway,
  Transferability, Status, Source — there is no endpoint column and no evidence-boundary column.
- **WHAT IT CAN ACTUALLY EXCLUDE →** nothing on its own; the mirror is a pointer. But it is also the
  surface a reader consults *instead of* the registry, and each of these three rows is the
  **de-qualified** form of a claim whose qualification is the whole point. `CLAIM 037`'s own boundary
  says the authors *"lasciano aperta la spiegazione (i topi potrebbero morire prima di
  convulsionare)"* and that **no EEG was run in the mouse**; the mirror says *"explicitly absent"*.
- **MORE SENSITIVE EVIDENCE →** not applicable — this is a propagation defect, the same class the
  registry already caught once: *"il mirror delle claim non si era mosso con le claim"*
  (`BATCH_20260810_005`).
- **VERDICT → `OVERSTATED`.** Three negative assertions travel in the mirror stripped of the
  endpoint qualifications that make them true, and the cross-cutting note converts the most heavily
  qualified of them into a portfolio-level conclusion (*"the threshold drops"*) one line below the
  table.

---

### 2.3 · `CANNOT ASSESS` — the claim does not state the endpoint its negative rests on

---

**`CLAIM 032` (leg C — human carrier parents)**

- **CLAIM →** *"Ogni famiglia umana pubblicata (Shaukat, Elsaadany, Abdel-Salam, Mallaret,
  Johannsen) ha **genitori portatori eterozigoti sani**."*
- **ENDPOINT USED →** **not stated.** The one quotation the claim supplies from that group of sources
  is *"no tumors were observed in the patient or **heterozygous mutation carriers**"* — a **tumour**
  observation. What "sani" means for the others — clinical impression at a genetics consultation,
  absence of a referral, a parent's own report — is not declared anywhere in the claim, in any of the
  cited records, or in the working model.
- **WHAT IT CAN ACTUALLY EXCLUDE →** unknown, because the instrument is unknown. Zero published WWOX
  carrier has a neuropsychological battery, an EEG or quantitative imaging.
- **MORE SENSITIVE EVIDENCE →** the only human monoallelic signal in the corpus is Leppa 2016
  (Geschwind, UCLA — fully independent of the field): heterozygous intragenic `WWOX` CNVs enriched in
  ASD multiplex families, *"low-penetrance ASD associated locus"*. 🔴 It is **explicitly refused as
  support** by the standing candidate — primary body unobtainable, the circulating OR is
  review-reported and two reviews by the same author disagree, and the CNV signal is
  **bidirectional** so duplications cannot evidence haploinsufficiency. It is recorded, not relied on.
- **VERDICT → `CANNOT ASSESS`.** This leg is **"nobody looked"**, not **"looked and found nothing"**,
  and the claim's wording does not distinguish them. Covered by the standing candidate; **no further
  proposal here.**

---

**`CLAIM 028` — *"expression level alone is insufficient to infer uniform functional benefit"***

- **CLAIM →** `Status: flagged for review`, `Type: INFERENZA — principio interpretativo trasversale`:
  *"Some systems suggest that **WWOX availability does not translate into simple linear benefit**
  unless relevant partners and network accessibility are preserved."* Its `Clinical meaning` is a
  cross-pathway brake: *"Impedisce di leggere «più WWOX = meglio» in modo lineare e uniforme.
  Rilevante per interpretazione di **terapia genica**…"*
- **ENDPOINT USED →** **none, anywhere.** `Source: papers 207, 218, 206, 214 (corpus 181–220)` —
  four corpus placeholders, no PMID, no assay, no system, no readout, no measured quantity. One of
  them, `CORPUS P206`, is documented in `CLAIM 023` as a placeholder whose `Identifier` was *"the
  literal string `PENDING`"*.
- **WHAT IT CAN ACTUALLY EXCLUDE →** indeterminate. Note the shape of the risk: this is a claim whose
  content is a **negative about monotonicity**, i.e. exactly the kind of statement that can only be
  earned by measuring an output at several input levels. Whether any of the four sources did that is
  not recorded.
- **MORE SENSITIVE EVIDENCE →** the corpus now holds two **fully-sourced, instrument-level**
  instances of the same principle that `CLAIM 028` asserts from placeholders: `CLAIM 034`
  (photoreceptor knockdown **lowers** superoxide, `PAPER 054`, with the counter-directional fly
  genetics of `PAPER 071`) and `CLAIM 002`'s rescue **overshoot** above wild type on CTIP2. Both
  already wikilink back to `CLAIM 028`.
- **VERDICT → `CANNOT ASSESS`.** A `flagged for review` interpretive brake that governs how gene
  therapy is read, resting on four unnamed placeholders with no endpoint. It is very probably **true**
  — that is not the finding. The finding is that **its truth is currently unauditable**, while two
  claims that could source it properly are already linked to it.

---

**`CLAIM 019` — *"livelli di trascritto WWOX normali"***

- **CLAIM →** *"Nei **fibroblasti di paziente**: **qRT-PCR → livelli di trascritto WWOX normali**"*,
  load-bearing for *"Il boost non è falsificato dalla sola normalità dell'mRNA, perché il collo di
  bottiglia potrebbe essere traduttivo"*.
- **ENDPOINT USED →** qRT-PCR, cell type declared (fibroblasts). **The amplicon is not declared** —
  neither in the claim, nor in `CLAIM 030`, nor in the working model.
- **WHAT IT CAN ACTUALLY EXCLUDE →** a change in abundance **of the region the primers amplify**. It
  cannot exclude an isoform shift, a 3′ or 5′ truncation outside the amplicon, or allele-specific
  imbalance — all of which would read as "normal total transcript". For a missense allele this is a
  small risk; the point is that it is **unstated**, and the model's own `CLAIM 018` establishes that
  WWOX alleles in this disease do produce exon-skipping transcripts.
- **MORE SENSITIVE EVIDENCE →** none run; allele-specific or junction-spanning RT-qPCR would settle
  it, and the registry already proposes exactly that instrument for a different allele (`CLAIM 033`,
  *"la RT-qPCR sulla giunzione esone 8→9 su cellule variant-carrying"*).
- **VERDICT → `CANNOT ASSESS`** — narrowly, on the amplicon. The rest of `CLAIM 019` declares its
  endpoints well and is not challenged.

---

**`CLAIM 033` (reserve 2) — *"no evidence to support an 'intermediate' phenotype"***

- **CLAIM →** *"Gli autori scrivono: «**no difference** between individuals with one or two missense
  variants… **no evidence to support an 'intermediate' phenotype**». La classe del genotipo di
  riferimento (`null/missense`) **non è risolta separatamente**."*
- **ENDPOINT USED →** **not stated.** The claim states the *statistical* limits thoroughly — *"N
  minuscoli per classe (`null/missense` n=15…); **nessun hazard ratio, nessun intervallo di
  confidenza numerico, nessuna mediana di sopravvivenza**"*, publication bias toward severe cases,
  survival confounded by supportive care — but never says **which variables** the authors' "no
  difference" was measured on, nor on what instrument they were scored.
- **WHAT IT CAN ACTUALLY EXCLUDE →** indeterminate. Since the dataset is *"aggregati da decenni di
  case report eterogenei"*, the plausible variables are exactly the coarse published descriptors —
  seizure presence, developmental level, survival — which is the class this audit is about.
- **MORE SENSITIVE EVIDENCE →** the claim's own **`Nota di direzione`** already supplies the correct
  inference and is worth preserving verbatim: misclassification is *"verosimilmente **non
  differenziale**"*, so *"il suo effetto atteso è di **diluire** la separazione vera"*, and
  *"La variabile biologica vera è la funzione residua; `null/missense` ne è l'ombra."*
- **VERDICT → `CANNOT ASSESS`** on the imported negative specifically. The claim's four mandatory
  reserves are among the best epistemic work in the registry; the one gap is that reserve (2) quotes
  an author-level negative without naming what it was measured on.

---

## 3 · Claims that are sound and why — the controls for this screen

An audit that finds everything broken is not an audit. **Twelve of the nineteen screened claims
handle their negatives correctly**, and several of them are the registry's own antibody against this
exact failure mode. They are listed with the same chain, compressed.

| Claim | The negative | Endpoint, as the claim declares it | Why it is `SOUND` |
|---|---|---|---|
| **`CLAIM 012`** | *"MRI precoce normale"* in a fatal neonatal case | early conventional MRI vs multifocal pathological EEG | 🔴 **The registry's canonical statement of this very principle.** It does not report a normal MRI as a normal brain — it concludes *"MRI normale in fase precoce **non esclude** disfunzione di rete severa"* and *"Rafforza EEG come endpoint **più sensibile** dell'imaging"*. `SOUND` |
| **`CLAIM 035`** | GSK3β inhibition proceeds with *"fosfo-GSK3β-S9 invariata"* | five orthogonal biochemical assays + a point mutation (L404) | 🔴 **The registry states the generalisation itself:** *"la de-repressione di GSK3β … sarebbe **invisibile a un western anti-fosfo-S9**, che è il saggio standard — qualunque studio WWOX-DEE che usi pS9 come readout di attività GSK3β produrrà un **falso negativo**."* This is the blunt-instrument rule already written into canon. `SOUND` |
| **`CLAIM 037`** | *"I topi Wwox-null **non hanno epilessia riportata**"* | Table 2 with an empty `Epilepsy` row; and `CLAIM 005` establishes that in the terminal source **no EEG, no seizure observation, no behavioural assay, no brain histology** was run | Distinguishes never-tested from tested-negative explicitly, keeps the authors' alternative (*"i topi potrebbero morire prima di convulsionare"*), and makes it testable against the rat's day-16 onset. **The textbook execution.** `SOUND` |
| **`CLAIM 005`** | NPY CA1/CA3 *"no obvious difference"* | *"the whole-hippocampus NPY panel carries **no significance marker** — a visual panel observation, **not a reported test**"*; IBA1/GFAP in DG *"marginal and unmarked"* | Refuses to promote an unmarked panel to a negative result. Also declares its positives' limits: *"Marker-positive abundance and area fraction — **not cell loss**, not glial cell number"*, and *"GAD65/67 is protein abundance only"* | `SOUND` |
| **`CLAIM 002`** | organoid size is a null; dorsal/ventral identity *"unchanged"* | ordinary one-way ANOVA + Tukey with **the p-values carried into the claim** (wk6 `0,3675` … wk18 `0,8952`; ventral `0,064`) | Names it *"a **performed and reported** test"* — the exact distinction this audit is hunting — and refuses to round `0,064` to nothing: *"non è significativo e **non è nulla**"* | `SOUND` |
| **`CLAIM 029`** | wild type carries the **highest** mutation burden | exome mutation burden, Supplementary Figure 1 | *"**Deliberately not stated as a reversal**"*; lists why the endpoint is weak (downstream, noisy, culture-history-dependent, exomes not genomes, filtered against all WT variants) and leaves the ATM mechanism untouched | `SOUND` |
| **`CLAIM 038`** | kidneys *"istologicamente normali"*, no proteinuria, no anaemia | light-microscopy renal histology + serum chemistry | Refuses to conclude "no renal dysfunction": keeps **both** competing explanations as `IPOTESI`, quotes the authors' own hedge, and names the discriminating experiment (renal clearance) **and the reason it was not done** | `SOUND` |
| **`CLAIM 036`** | osteosarcoma *"0/9 by multimodal examination"* | gross + histological examination vs μCT | 🔴 Records the field's own blunt-instrument dispute **and refuses its untested resolution**: *"failed to detect osteosarcomas … **most likely due to the lack of a sensitive detection method such as μCT**"* is tagged `PREMISE: DEFAULT_FROM_TEXTBOOK` with a `REVIVAL_TRIGGER` (μCT re-imaging of archived limbs). Also catches the positive side's 86%-asserted-as-100% | `SOUND` |
| **`CLAIM 023`** | no experiment couples phosphorylation to localisation | **machine-checkable**: *"20 sentences in the body mention Src, and **ZERO** of them also mention localisation, cytoplasm, nucleus, redistribution or sequestration"*, confirmed by two blind auditors with a ±400-char proximity screen | Converts "never tested" from an impression into a count, then narrows the **title** and leaves the binding leg — the best-supported content — at `consolidated baseline`. **This is the model this audit's own recommendations should follow** | `SOUND` |
| **`CLAIM 003`** | *"gli oligodendrociti **non sono mai trasdotti**"* | CC1 / anti-WWOX co-staining | Endpoint declared; the conclusion is deliberately scoped to *"**una componente**, non l'intero fenomeno"*, and the residual gap is kept as `DATO` while the authors' oligodendrocyte attribution is tagged their `IPOTESI` | `SOUND` |
| **`CLAIM 004`** | no tumours observed after AAV9 rescue | *"il non-rilievo di tumori qualificato **tre volte** (*gross*, *limited number*, *8–11 months*) in un oncosoppressore con periferia ancora null"* | The endpoint is named and triple-qualified in the claim's own text. ⚠️ **One gap worth noting, not a defect:** the instrument is *gross* necropsy, and `CLAIM 036` records a live, untested allegation that gross/histology misses Wwox-associated osteosarcoma where μCT finds it. The two claims do not cross-reference | `SOUND`, with a missing cross-link |
| **`CLAIM 014`** | Tochigi excluded from the prenatal leg | *"**PMID 31340538 (Tochigi) contributes early postnatal maturation and hypomyelination at PND5–21 — not prenatal migration, not cortical layering** … It measures no prenatal time point."* | The conclusion is **right** and the prenatal leg correctly rests on Iacomino and Kośla instead. ⚠️ **What is absent is the reason it is right:** that paper did not merely fail to measure migration, it **affirmatively denied it** — *"Wwox is **not required** for proliferation and migration of immature neurons"* — on bulk NeuN, and the **same investigators overturned it one year later** with Satb2/Tbr1 and E16.5 BrdU. The corpus's cleanest worked example of this failure mode is not recorded in canon | `SOUND`, with a high-value addition available |

**One coverage note, not a verdict.** `CLAIM 021` (Breton 2021, `consolidated baseline`) is sound for
its stated scope — neuron-specific `Wwox` loss, neocortical slice LFP and patch-clamp. But its source
contains the **strongest independent heterozygote signal in the literature** (4/23 het slices vs 0/11
WT) and `CLAIM 021` does not carry it, because in that paper the het is *"frequently pooled with WT
into `S-CTL`"*. The same structure recurs across the field: Tochigi pools `+/+` with `+/lde` as
"normal"; `PAPER 058` reports `0/14 controls` with the control genotypes undifferentiated; the
Aqeilan colony is bred het × het, so ~15 CNS papers had het littermates and the only het data ever
published from it are fertility rate and litter size. **The heterozygote phenotype is not absent from
the literature — it is inside the control groups.**

---

## 4 · Ranked list — which findings would justify a commit candidate

For the orchestrator to decide. **Nothing is proposed for `CLAIM 032`**, which is already covered by
`CC-20260920-CLAIM032-ENDPOINT-QUALIFIER-01`.

| # | Finding | What a candidate would propose | Class |
|---|---|---|---|
| **1** | **`CLAIM 030`: *"proteina assente"* for Q230P, where `CLAIM 019` and the working model both say *"non rilevata" / "not detected"*.** The claim whose thesis is that abundance does not report function converts a blot's detection floor into an absolute, and that absolute feeds the *"funzionalmente null/null"* prognostic limb. | Replace *"proteina assente"* with *"proteina non rilevata al western (fibroblasti di paziente)"*, aligning `CLAIM 030` to `CLAIM 019` and to BLOCK 1; add a `PREMISE_TAG` that non-detection at a blot's floor is not absence, and a `REVIVAL_TRIGGER` on targeted MS or on `CLAIM 035`'s GSK3β/Tau functional assay. **No status change, no conclusion challenged** — `CLAIM 030`'s thesis is *strengthened* by the correction. | **MINOR** |
| **2** | **`CLAIM 039`: the title asserts *"it is not cerebellar"* on unblinded light-microscopy histology**, and the working-model mirror repeats the exclusion with no endpoint. This is the `CLAIM 023` situation exactly — a faithful summary under an over-welded title. | Narrow the title to what the endpoint supports (*"…with no gross cerebellar histopathology; the anatomical substrate is unresolved"*), keep the 95%-vs-0% finding and `Status: in observation` untouched, and propagate the narrowed wording into BLOCK 2 row 039. ⚠️ Precedent for the method: `CLAIM 023`, `BATCH_20260909_001`. | **ORDINARY** (title narrowing on an `in observation` claim) |
| **3** | **A new entry in `DEFAULTS THAT BIT US`.** The ledger has no default covering endpoint sensitivity — `D-14` covers figure captions, `D-15` citation attribution, `D-01`–`D-04` biochemistry. The pattern found three times in one batch, and four more times in this audit, has no home. | Add `D-NN — *a normal result on a coarse endpoint is a normal phenotype*`, with the three batch instances as its cost column and the rule: **before recording any negative, state the instrument and ask what it could not have seen; a negative with no named instrument is "nobody looked", not "looked and found nothing."** This is the highest-leverage item because it is preventive and applies to every future reading. | **MINOR** (append-only ledger) |
| **4** | **`CLAIM 014`: the NeuN worked example is missing from its own evidence boundary.** The boundary's conclusion is right; the reason — an affirmative negative on bulk NeuN, overturned by the same investigators with Satb2/Tbr1 and E16.5 BrdU — is the cleanest instance of the failure mode the corpus owns, and it is nowhere in canon. | Add the two verbatim quotes and the one-year reversal to `CLAIM 014`'s existing evidence boundary. **Strengthens the claim**: it converts "this paper is silent on migration" into "this paper's negative on migration was retracted by its own authors on a better instrument." No status change. | **MINOR** |
| **5** | **`CLAIM 013`: an MRI null reported without the `CLAIM 012` cross-reference that defuses it.** The registry holds, at `consolidated baseline`, that early MRI underestimates this disease; `CLAIM 013` lists an MRI null among its non-findings without saying so. | Add one sentence and a wikilink to `CLAIM 012` / `CLAIM 015`, and mark the four nulls as **floors under a parental-survey instrument**, not negatives. No status change, no statistic touched. | **MINOR** |
| **6** | **The BLOCK 2 mirror carries three de-qualified negatives (rows 032, 037, 039).** A reader who consults the mirror instead of the registry gets *"not deleterious"*, *"explicitly absent"* and *"not cerebellar"* with no endpoint and no boundary. | Either add an endpoint/qualifier column to the mirror, or append the `🔴` marker already used for row 011 to rows 032/037/039 so the qualification is visible at mirror level. Precedent: `BATCH_20260810_005`, which fixed the mirror for exactly this reason. **Sequence after items 1–2**, so the mirror is updated once. | **MINOR** |
| **7** | **`CLAIM 028` rests on four unnamed corpus placeholders and states a negative about monotonicity.** Already `flagged for review`. Two properly-sourced instances (`CLAIM 034`, `CLAIM 002`'s CTIP2 overshoot) already wikilink to it. | **Do not resolve by rewriting.** Propose a sourcing task: resolve `CORPUS P207/P218/P206/P214` to identifiers, or re-found `CLAIM 028` on `CLAIM 034` + `CLAIM 002`, which would earn its status. Lowest rank because nothing downstream is wrong — the principle is almost certainly true. | **sourcing task, not a claim edit** |

**Not proposed, deliberately:** anything touching `CLAIM 032` (covered); any reversal, demotion or
status change on any claim; any therapeutic implication. Every item above either **narrows a scope to
its endpoint** or **adds a qualifier**, and item 4 **strengthens** its target.
