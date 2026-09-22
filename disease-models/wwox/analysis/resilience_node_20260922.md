# RESILIENCE NODE — the conditional-deletion ladder: which compartments tolerate cell-autonomous WWOX loss, and why?

**Node:** `COMPARTMENT_RESILIENCE_LADDER` · **Actor:** Scientist C · **Date:** 2026-09-22
**Status:** non-canonical analysis file. No canonical file edited, no registry written, no receipt
claimed, no commit, no git command run, no external contact made.
**Read-only toward every canonical file.**

> 🔴 **NOTHING IN THIS FILE IS MEDICAL ADVICE.** No molecule, class, dose, route, schedule or
> compound screen is named anywhere in it. A mechanistic hypothesis is not a treatment. No generic
> neuroprotection is proposed or implied.
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is
> described and no contact detail of any living person is reproduced.
>
> 🔴 **Alleles, drivers and species are never pooled.** `Wwox`-null (Aqeilan strain),
> `Wwox^ΔCre/ΔCre` (EIIA-Cre, Aldaz strain), the NCKU nulls, `gt/gt` hypomorph, `P47T` knock-in,
> `P47R`, `G372R`, `Q230P`, Synapsin-Cre `S-KO`, Nestin-Cre `N-KO`, Olig2-Cre, GFAP-Cre, BK5-Cre,
> Alb-Cre `Wwox^hep−/−`, adipocyte-Cre, ACTA1 `Wwox^ΔSKM`, rat `lde/lde`, human WOREE and human
> SCAR12 are **different objects** and appear in different rows throughout.

---

## 0 · BASELINE — enumerated first, filtered second

**What was enumerated before any question was formed.** Plain `ls` of
`disease-models/wwox/analysis/` (**167 entries**, read end to end, including the four subdirectories
`data/`, `near_miss_cases/`, `orchestration_reviews/`, `scripts/`) and full recursive
`ls -R disease-models/wwox/research/` (**9 subdirectories**; 54 dossiers, 100 deepdive manifests,
117 commit candidates, 43 session evaluations). Only after the whole listing was read were greps
run.

**The seven files I was told already occupy this territory were read before anything was proposed,
and none is re-derived here:**

| File | What it settles | Consequence for this node |
|---|---|---|
| `resilience_and_modifier_census_20260921.md` | Modifier search across human outliers, discordant sibs, mouse strains, paralogue — **NEGATIVE**. No discordant sibling pair exists; mouse survival differences are confounded by allele, targeting, Cre driver and species; WWOX has no paralogue. `:142` records sex as *"not addressed as a modifier anywhere"* but logs the `lde` female-only audiogenic cohort as a **confound, not an effect** | 🔴 **Not re-run.** This node does **not** ask which *individual* or which *strain* is spared. It asks which **cell/tissue compartment** is spared — a question that census did not pose and its negative does not cover |
| `downstream_wwox_independent_rescue_census_20260921.md` | Bounded census of downstream rescue; four positive arms in the whole literature; the ethosuximide/SWD wave | Not reopened |
| `wwox_independent_downstream_rescue_20260922.md` | The **A–L node map**, the selectivity audit, outcome-width scoring, top three (G3, Tau polymer, Kir4.1/AQP4) | Used as the **occupancy map**. I propose no new row of it. §5 argues about how one existing row (**G1**) was scored, not about its mechanism |
| `new_discovery_node_20260922.md` | Subfield-selective vacuolation in the `lde/lde` hippocampus; H0–H6 + the H5a/H5b fork; E1–E5 | 🔴 **Not re-entered.** Its `E1`, `E2`, `E5` remain that file's, unnamed and unclaimed here |
| `lde_myelin_vacuole_bridge_20260922.md` | The bridge — **CANNOT BE ADJUDICATED FROM HELD MATERIAL**; regional surrogate runs against it; `H5a` weakened, `H5b` survives by non-elimination | Verdict accepted. §0.1 states why I did **not** take the operator's suggested restart |
| `mechanism_intervention_map.md` | M-nodes, N-/R- portfolio, the DEPRIORITIZE list (incl. **N-13 pro-myelinating**, **N-08 DCA**, **N-01 mTOR**, **N-14 antioxidants**) | Treated as closed. Nothing here re-proposes a deprioritised class |
| `earliest_lesion_developmental_timeline_20260921.md` | Earliest-lesion timeline; prenatal mapping not supportable; zero prenatal intervention in any WWOX model | Not re-derived |

**Also read before proposing:** `superior_node_search_20260922.md` (three whole-session node
searches already exist; `:74` records **pro-myelinating / OPC maturation** as *"already held and
rejected — wrong cell compartment, closing window"*), `next_node_scout_20260921_orchestrator.md`,
`scientist_node_scouting_20260920.md`, `DISCOVERY_TRACE_metabolic_gating_20260922.md` (self-graded
**REDISCOVERY**; its §7.4 question — *how does a CNS-only vector rescue a death with peripheral
components* — and its §7.5 experiment are **that file's and are not re-proposed**),
`wwox_myelin_oligodendrocyte_census_20260921.md`, `peripheral_phenotype_denominator_audit_20260922.md`,
`AUTONOMOUS_SESSION_STATE.md` (sixth block).

### 0.1 Why I did not restart from hypomyelination-alone or vacuolation-alone

The operator offered both as legitimate independent restarts. I declined both, for a stated reason
rather than a preference:

- **Hypomyelination alone** lands inside `wwox_independent_downstream_rescue_20260922.md` row **E**
  (`:103`) and `superior_node_search_20260922.md:74`, where the class is already **rejected on
  compartment** — *"the OPCs are present and not receiving the axonal signal"*. Reopening it
  without a new variable is re-derivation.
- **Vacuolation alone** is the whole object of `new_discovery_node_20260922.md`, whose H0 —
  *the sparing has never been counted* — is unresolved. A second file on the same unmeasured
  observation adds hypotheses to a table that is already seven rows long and gated on one count.

**What I took from the operator's framing instead** is its shape, not its two candidates: *a spared
compartment next to a failing one under comparable WWOX loss*. The repository holds that comparison
in a **cleaner** place than the hippocampus — in genetics, not in histology.

### 0.2 The gap the enumeration actually exposed

`grep` across every markdown file in `disease-models/wwox/`:

- **`FT-049` is developed in no analysis file anywhere.** It is registered at
  `research/full_text_queue_current.md:1404` as *"il tessuto di misura non è il tessuto di
  necessità"* — priority **ALTA**, epistemic status **`INFERENZA`**, three first-hand-read sources,
  and an explicit terminal note: *"Non può salire a `DATO` senza un esperimento che testi la
  dissociazione compartimento/necessità in modo diretto"*. **That experiment has never been
  designed.** Outside the queue, `FT-049` appears only as a pointer in
  `framework/state/state_manifest_current.md`, one dossier, one commit candidate, one session
  evaluation and one crosswalk — **never as the object of an analysis.**
- **No file in the repository assembles the conditional-deletion lines into a single vulnerability
  table.** `peripheral_phenotype_denominator_audit_20260922.md:18-22` lists the drivers, but as a
  **non-pooling firewall declaration**, explicitly so that they stay in *different rows*. Listing
  objects so they are never compared is the opposite of comparing them.
- **No file offers any explanation for the Olig2-Cre and GFAP-Cre negatives.** They are used
  everywhere as evidence *that* the myelin defect is non-cell-autonomous, and nowhere as a datum
  about the **oligodendrocyte's and astrocyte's own tolerance of WWOX loss**.
- 🎯 **Two first-hand-read data from `PMID 30755385` are used nowhere in the repository.** `soleus`,
  `soleo`, `EDL`, `slow-twitch` and `fibre lente` return **zero hits** outside that paper's own
  dossier. One of them is a within-animal WWOX-abundance-versus-vulnerability gradient — the
  scarcest kind of evidence this node needs.

**That is the node.** Not a new mechanism: a **comparison the repository has structurally forbidden
itself from making**, and which its own `FT-049` says must be made.

---

## 1 · THE OBSERVATION, STATED WITHOUT INTERPRETATION

**The ladder.** Every row is a *cell-autonomous* deletion of `Wwox` restricted to one compartment,
or a compartment-restricted restoration. 🔴 **No row is pooled with any other; each carries its own
driver, strain and endpoint set, and the endpoint sets are not the same.** That non-equivalence is
itself hypothesis `R5` in §2 and is not hidden.

| # | Compartment · driver | Outcome of cell-autonomous WWOX loss | Depth in LEGEND |
|---|---|---|---|
| **L1** | **Hepatocyte · Alb-Cre `Wwox^hep−/−`** | 🟢 **TOLERATES (for the measured endpoints).** Does **not** lower circulating HDL-C in either sex — the phenotype appears only in the whole-body null | 🟢 first-hand: `PMID 24871327`, `complete_fulltext_read`, receipt `FTR-20260810-24871327-01`, dossier `research/fulltext_dossiers/PMID24871327_locators.md` |
| **L2** | **Hepatocyte · Alb-Cre** (second study) | 🟢 **TOLERATES.** In a three-way comparison of hepatocyte, adipocyte and skeletal-muscle deletion, *"solo il KO muscolare altera GTT e peso"* | 🔴 SIBLING-ATTESTED — `research/fulltext_dossiers/PMID30755385.md:47` and `:67` (paper read in full, `reading_state.md:107`) |
| **L3** | **Adipocyte · adipocyte-Cre** | 🟡 **TOLERATES, weakly evidenced.** Same negative three-way comparison; the adipose negative is *"blot rappresentativo, `n=3`, risoluzione nativa bassa e nessuna quantificazione"* | 🔴 SIBLING-ATTESTED — `research/fulltext_dossiers/PMID30755385.md:97` and `:106-108` |
| **L4** | **Skeletal muscle · ACTA1-rtTA;tetO-Cre `Wwox^ΔSKM`** | 🔴 **FAILS.** Fasting hyperglycaemia, impaired GTT, weight gain; fat mass ↑ / lean mass ↓; HDL/LDL ↓, TG + cholesterol ↑; reduced `18F-FDG` uptake in gastrocnemius and hamstring; reduced mtDNA, Krebs-cycle transcripts and slow-twitch transcripts; reduced p-AMPK^Thr172^ and p-ACC; HIF1α, PKM2, PDK1, LDHA1, MCT4 up | 🔴 SIBLING-ATTESTED — `research/fulltext_dossiers/PMID30755385.md:67-81` |
| **L5** | 🎯 **Within L4 — fibre type** | **WWOX immunofluorescence is more intense in soleus than in EDL** (Fig. S4, read as pixels at 512 ppi), and what the knockout loses includes the **slow-twitch transcript programme** | 🔴 SIBLING-ATTESTED — `research/fulltext_dossiers/PMID30755385.md:96` and `:78` |
| **L6** | 🎯 **Within L4 — other organs of the same animal** | `18F-FDG` uptake *"non rilevato come diverso in cervello o fegato"* | 🔴 SIBLING-ATTESTED — `research/fulltext_dossiers/PMID30755385.md:72-73` |
| **L7** | **Neuron · Synapsin-Cre `S-KO`** | 🔴 **FAILS.** Spontaneous neocortical bursting, altered oscillatory organisation, ↑phase–amplitude coupling, ↑excitatory drive, ↓spontaneous inhibition | 🟢 `CLAIM 021` read directly, `registries/claim_registry_current.md:382-392` (source `PMID 34634460`, receipt on file) |
| **L8** | **Neuron · Synapsin-Cre; progenitor · Nestin-Cre** | 🔴 **FAILS.** Reproduce the phenotype **including the myelin defects** | 🟡 **SECOND-HAND — see §1.1.** `CLAIM 003`, `registries/claim_registry_current.md:67-79`; `PAPER 004` = `PMID 33914858` |
| **L9** | **Oligodendrocyte · Olig2-Cre; astrocyte · GFAP-Cre** | 🟢 **TOLERATE.** *"produces no evident abnormality"* | 🟡 **SECOND-HAND — see §1.1.** Recorded at `analysis/wwox_myelin_oligodendrocyte_census_20260921.md:36-42` and `analysis/wwox_independent_downstream_rescue_20260922.md:103` |
| **L10** | **Neuron-restricted *restoration* · AAV9-hSynI-WWOX** | Corrects **peripheral** phenotypes, hypoglycaemia included, with oligodendrocytes **never transduced** and myelin improving anyway; rescue **incomplete** against WT | 🟢 `CLAIM 004` read directly, `registries/claim_registry_current.md:84-100` (`PMID 34747138`, receipt `FTR-20260810-34747138-01`) |

### 1.1 🔴 UNDISCHARGED READING DEBT — declared before it is leaned on

**`PMID 33914858` (Repudi 2021, *Brain*) has NO read receipt in this repository.** It is declared in
the registry as `PAPER 004` (`registries/paper_registry_current.md:95-107`, status `integrated`), and
`CLAIM 003` is a `consolidated baseline` claim sourced to it — so citing the **claim** is legitimate.
But the **conditional-Cre content of rows L8 and L9 reaches LEGEND second-hand**, through another
paper's summary (Obeid 2026), as
`analysis/wwox_myelin_oligodendrocyte_census_20260921.md:36-42` states in terms: LEGEND holds that
result *"only second-hand"*, and the census's own remedy is to acquire the paper *"to verify the
attribution, not to learn the answer"*. The repository separately records that this PDF's text layer
is corrupted (`FT-044` suspended after *"P < 0.05"* extracted as *"P 5 0.05"*).

> 🔴 **Consequence, applied throughout and not softened:** **no conclusion in this file rests on L8
> or L9.** They appear in the ladder because omitting them would misrepresent the evidence, and every
> hypothesis in §2 is scored twice — once with them, once without — in §7.2. The node survives
> without them; it is *sharper* with them, and that sharpness is debt, not evidence.

### 1.2 Why this is worth a node at all

**Because the comparison is genetic, not histological.** Every other "why is this spared" question in
this repository — hippocampal subfield, cerebellar layer, Purkinje cell, regional myelin — rests on
reading an image. This one rests on **eight conditional alleles** in which an experimenter removed
the same gene from a named compartment and measured what happened. Three compartments tolerated it;
two did not; and within the one tissue where WWOX was localised at fibre resolution, **the compartment
carrying more WWOX is the compartment whose programme is lost**.

🔴 **And the repository's own rule says this comparison is owed.** `FT-049` is `INFERENZA` at priority
**ALTA** with the note that it cannot become `DATO` without a direct compartment/necessity experiment.
**Designing that experiment is what §6 does.**

---

## 2 · DIVERGE — six mechanistically distinct explanations

**Distinct = predicts a different measurement.** The discriminator column is the value of this table.
Nothing here is offered as established; every row is `IPOTESI` unless its cell says otherwise.

| # | Mechanism | What makes it distinct | 🎯 The readout that separates it from its neighbours |
|---|---|---|---|
| **R1** | **OXIDATIVE-DEPENDENCE GATING.** Vulnerability is set by how much a compartment depends on mitochondrial ATP. WWOX loss forces a glycolytic shift; a cell that can live glycolytically (hepatocyte, adipocyte, and — if L9 holds — oligodendrocyte, astrocyte) is spared; a cell that cannot (oxidative myofibre, neuron) fails | Locates resilience in **fuel strategy**, and predicts it is a property of the *state*, not of the cell identity | 🎯 **Respirometry / OCR:ECAR per compartment, plus a state-change arm.** R1 uniquely predicts that a **resilient** compartment can be made **vulnerable** by forcing it into oxidative metabolism, and that the vulnerable one is protected by substrate availability. **No other row predicts a reversible vulnerability.** Cheap surrogate available today: oxidative-enzyme histochemistry (SDH/COX) mapped onto lesion location within one tissue |
| **R2** | **EXPRESSION-DOSE GATING.** Vulnerability tracks how much WWOX protein the compartment normally carries. Lose more, lose more function | Puts the explanation in the **wild-type baseline**, requiring no lesion mechanism at all | 🎯 **Cell-type-resolved WWOX protein in wild type**, quantified against lesion severity across L1–L9. **L5 is the only existing measurement of this kind and it SUPPORTS R2** (soleus > EDL). R2 predicts a **monotonic** abundance–severity relation; R1 predicts abundance may be **flat or inverted** where fuel strategy differs |
| **R3** | **RENEWAL GATING.** Resilient compartments replace damaged cells (hepatocyte, adipocyte, OPC pool); vulnerable ones are **post-mitotic and long-lived** (myofibre, neuron). The phenotype is a failure to *clear*, not a failure to *function* | Makes resilience an **organ-level** property, invisible in any single-cell assay | 🎯 **Turnover + damage markers, and one perturbation nothing else needs:** apoptosis/proliferation indices in each deleted compartment, and whether **blocking regeneration unmasks a hepatocyte phenotype**. R3 alone predicts a latent, unmasking-dependent lesion in a "resilient" tissue |
| **R4** | **PARTNER-AVAILABILITY GATING.** WWOX has no paralogue, but its PPxY/WW-domain and SDR-span partner sets differ by cell type; a compartment lacking the relevant partner has nothing to lose | Puts the explanation in the **interactome**, not in metabolism or dose | 🎯 **Cell-type expression of the partner set** (the repository's own SDR-span and WW1 partner inventories) against the ladder. R4 predicts severity tracks **partner presence with WWOX abundance held constant** — the one pattern R2 cannot produce |
| **R5** | 🔴 **THERE IS NO LADDER.** The negatives are endpoint-limited and underpowered, not biological: L1 was never given a CNS or muscle endpoint, L3's negative is an unquantified `n=3` blot, and *"no evident abnormality"* (L9) is a phrase, not a panel | **Denies the explanandum entirely** | 🎯 **A per-Cre-line endpoint matrix**: for every published WWOX conditional line, which endpoints were actually run, with what n and what comparator. R5 alone predicts that the "resilient" rows are the rows with the **fewest and least sensitive endpoints**, and it is falsified the moment a resilient line is shown to have been given the same panel as a failing one |
| **R6** | **TIMING, NOT CELL TYPE.** The drivers differ in onset relative to the WWOX-critical window — Alb-Cre, adipocyte-Cre, ACTA1-rtTA (doxycycline-dependent, inducible), Olig2-Cre, Synapsin-Cre and Nestin-Cre do not delete at the same developmental moment. Resilience is an artefact of *when*, not *where* | Makes the ladder a **chronology**, and predicts the cell-type axis is epiphenomenal | 🎯 **Cre-onset age versus phenotype severity**, plus the one decisive design: a **single inducible driver deleting at two different ages in the same compartment**. R6 predicts severity tracks onset with cell type held constant; every other row predicts the opposite |

### 2.1 Rival elimination already available from held material, before any new experiment

- 🎯 **`L5` and `L6` together weaken `R5` and `R6` in one stroke, and this is the most useful thing
  in the table.** Both are **within the same animals, under the same driver, at the same onset, in
  the same experiment**. The vulnerability gradient between soleus and EDL, and the absence of an
  FDG deficit in brain and liver of the very animal whose muscle is affected, cannot be explained by
  a different Cre, a different age or a different endpoint panel — **there is only one of each.**
  R5 and R6 remain live for the *cross-line* rows; they are **excluded for the within-animal rows**.
- 🟡 **`L5` supports `R2` and is consistent with `R1`**, because soleus is both the WWOX-richer and
  the more oxidative fibre. 🔴 **Stated against my own preference: soleus does not dissociate the two
  variables, so L5 cannot rank R1 against R2.** Any design that uses it must add a compartment where
  abundance and oxidative character come apart. §6 does exactly that and nothing less would.
- 🔴 **`R3` is weakened by `L4`.** The skeletal myofibre is post-mitotic, but so is the neuron, and
  the tissue that failed here failed with a **metabolic and transcriptional** signature
  (mtDNA, Krebs transcripts, p-AMPK), not a degenerative one. R3 predicts damage-and-clearance; the
  measured phenotype is programme loss. **Weakened, not killed** — no turnover index was measured.
- 🔴 **And one thing the ladder does NOT show, stated so it is not over-read.** `L1`/`L2` are
  negatives for **HDL-C, GTT and body weight**. They are **not** negatives for liver function in
  general: a third study reports serum ALT ≈2× in `Wwox^hep−/−` under a high-fat diet
  (`analysis/peripheral_phenotype_denominator_audit_20260922.md:91`, `:164`). 🎯 **The hepatocyte is
  not unconditionally resilient — it is resilient at baseline and reportedly not under metabolic
  challenge.** That observation is `R1`'s single best existing foothold and it was found in the
  repository, not in the primary.

---

## 3 · CONNECT — one adjacent field, both halves

**Field of origin: the cell-type-selectivity problem in mitochondrial disease**, specifically the
**NDUFS4** conditional-knockout ladder in Leigh syndrome. 🔴 **Protein and system of origin carried
throughout: NDUFS4 is an accessory subunit of mitochondrial respiratory complex I, in the mouse. It
has no relationship of any kind to WWOX — no shared complex, pathway, domain, family or interactor.**

### ✅ WHAT TRANSFERS

1. **The ladder as a method, and its known failure mode.** That literature ran precisely this design
   — whole-body null versus neuron-restricted versus glia-restricted deletion of one gene — and
   established a discipline for reading it: a compartment-restricted negative is read as *"this
   driver, this onset, this panel produced no detected phenotype"*, never as *"this cell type does
   not need the gene"*. **That is `R5`, borrowed as a method and not as a result.**
2. **The precedent that a "glial negative" is the row most likely to be revised.** In that field the
   glial arms were repeatedly the ones whose negatives narrowed once a more sensitive endpoint or a
   different driver was used. 🎯 **This is why `L9` is the row I refuse to build on**, independent of
   its reading debt — two independent reasons to hold it, not one.
3. **The design principle that a within-animal gradient outranks a cross-line comparison**, because
   it holds driver, onset and panel constant. That principle is what makes `L5`/`L6` load-bearing
   here and the cross-line rows merely suggestive.

### ❌ WHAT DOES NOT TRANSFER

1. 🔴 **No mechanism transfers.** NDUFS4 has a defined biochemical lesion — a named subunit of a
   named complex with a measurable assembly and activity defect. **WWOX has no defined physiological
   substrate and no validated catalytic readout for any disease allele**, which this repository
   records independently (`TX-003`; `analysis/function_per_molecule_assay_design_20260922.md`).
   Importing a complex-I interpretation into a WWOX phenotype would be a category transfer. **`R1`
   is a hypothesis about fuel dependence, NOT a claim that WWOX is a respiratory-chain protein.**
2. 🔴 **No phenotype maps.** Leigh syndrome's neuropathology is bilateral symmetrical brainstem and
   basal-ganglia necrosis. Nothing in the WWOX corpus reports that distribution in any model or in
   any human genotype class. **No anatomical expectation may be imported.**
3. 🔴 **No therapy transfers, and none is named.** That field's intervention classes are not
   mentioned here, are not implied here, and are not made admissible by this analogy.
4. 🔴 **The analogy cannot supply evidence, only design.** If §7 finds that the WWOX ladder behaves
   unlike the NDUFS4 ladder, that is a fact about WWOX, not a failure of the WWOX data.

---

## 4 · HYPOTHESIS AND PREREGISTERED PREDICTIONS

> 🔴 **§4 was written to disk in full, with §5 EMPTY, BEFORE any confirmatory search was run.**
> Nothing in §4 was edited afterwards. Being wrong is acceptable; retrofitting is not.

**Working ranking, which is itself a prediction:**
`R5` ≳ `R6` > `R1` ≈ `R2` > `R3` > `R4`.

**I expect the ladder to be substantially an artefact of unequal endpoint panels and unequal Cre
onset**, and I expect that what survives that deflation is a **within-animal** gradient (L5/L6)
rather than a cross-line one. I am fixing this before looking because it is the *opposite* of the
conclusion the ladder invites, and the invited conclusion is the one I would most enjoy writing.

| # | Prediction (falsifiable) | How it will be scored |
|---|---|---|
| **P1** | **No published study applies the same endpoint panel to a WWOX-resilient and a WWOX-vulnerable conditional line.** The comparison in `L2` (hepatocyte vs adipocyte vs muscle, one panel, one paper) will prove to be the **only** matched-panel comparison in the entire WWOX literature | SUPPORTED if no second matched-panel comparison is findable; REFUTED if one exists |
| **P2** | **No WWOX conditional line has ever been given a neurological or CNS endpoint except the neural drivers themselves.** No Alb-Cre, adipocyte-Cre or ACTA1 animal has been EEG'd, behaviourally phenotyped or had brain histology | SUPPORTED if no such endpoint is findable in any surface |
| **P3** | **No WWOX study anywhere has measured oxygen consumption, extracellular acidification or respiratory flux in any compartment** — the `R1`-versus-`R2` discrimination has no existing data in this gene, in any species | SUPPORTED if no respirometry/flux measurement is findable; REFUTED if any exists |
| **P4** | 🎯 **`L5` (soleus > EDL WWOX immunofluorescence) has never been cited, reused or reasoned from by anyone** — not in the WWOX literature and not in this repository | SUPPORTED if no reuse is findable; the repository half is already measured (zero hits) |
| **P5** | **The hepatocyte "resilience" of `L1` will prove conditional, not absolute** — at least one report of a `Wwox^hep−/−` phenotype under challenge exists | SUPPORTED if such a report exists (the ALT-under-HFD datum already suggests it); REFUTED if the hepatocyte is negative under every tested condition |
| **P6** | **No WWOX conditional line has been deleted at two different ages under one inducible driver**, so `R6` cannot be adjudicated from any published WWOX experiment | SUPPORTED if no two-age induction is findable |
| **P7** | 🔴 **Against my own hypothesis `R1`:** if `R1` were right, the human WWOX-deficient brain should show a glycolytic/oxidative imbalance. I predict the held human evidence will run **AGAINST** it — the repository records human metabolism as normal on four independent screens, with a single cerebral-MRS outlier in the **wrong direction**. I expect this to survive checking and to **weaken `R1`** | SUPPORTED if the human counter-evidence is confirmed as I have described it, which weakens R1; REFUTED if I have mis-stated it |

---

## 5 · RESULTS OF THE CONFIRMATORY SEARCH

> **Method of scoring.** Every prediction below is scored against searches run **after** §4 was on
> disk. 🔵 **Source attribution: bibliographic records, query counts and abstracts in this section
> were retrieved from PubMed.** No prediction was rewritten, none was softened, and the one that
> failed is marked as failed.
>
> ⚠️ **A query census is a statement about what a query returns, not about biology.** This
> repository has documented **five** ways a query-count zero lies, and the fifth is the dangerous
> one: *a reagent named only in Methods is invisible to `[All Fields]`* (`AUTONOMOUS_SESSION_STATE.md`,
> sixth block). 🔴 **That defect is live here and I measured it rather than assuming it away:**
> `Wwox AND (conditional OR floxed OR Cre) AND (knockout OR deletion)` returns **10** records and
> **omits every conditional line this node is built on** — `PMID 33914858`, `PMID 30755385`,
> `PMID 24871327`, `PMID 34747138` are all absent, against a positive control `Wwox[tiab] AND
> mice[tiab]` → **99**. **Every negative below is therefore an upper bound on what a query can see,
> not a statement that the experiment does not exist**, and each is given with its positive control.

| # | Score | Evidence |
|---|---|---|
| **P1** | 🟡 **SUPPORTED, weakly** | No second matched-panel comparison is findable. The hepatocyte-vs-adipocyte-vs-skeletal-muscle comparison of `PMID 30755385` — one panel, one paper, one figure series — remains the only place in the WWOX literature where a resilient and a vulnerable compartment meet the **same** endpoints. 🔴 **Bounded by the instrument defect above:** the query that should have enumerated the conditional lines could not see four of them, so this negative is weak by construction and is recorded as such |
| **P2** | 🟡 **SUPPORTED, weakly** | `Wwox AND (EEG OR seizure OR behaviour OR behavior OR cognition) AND (liver OR muscle OR adipose OR hepatocyte)` → **7** records, **none** of which is a non-neural conditional line given a CNS endpoint. **No Alb-Cre, adipocyte-Cre or ACTA1 animal has been EEG'd, behaviourally phenotyped, or had brain histology reported.** Same bound as P1 |
| **P3** | 🔴 **REFUTED — and it is refuted against me** | `WWOX AND (oxygen consumption OR Seahorse OR respirometry OR extracellular acidification OR oxidative phosphorylation)` → **4** records, and three of them measure or genetically probe exactly what I predicted nobody had. According to PubMed: **PMID 26390919** (Choo, O'Keefe, Richards *et al.* 2015, *Genes Chromosomes Cancer*, [DOI](https://doi.org/10.1002/gcc.22286)) — *"Altered WWOX levels modulate variable cellular outgrowths caused by genetic deficiencies of components of the mitochondrial respiratory complexes"*, *"This modulation requires the enzyme active site of WWOX"*; **PMID 23765596** (Dayan, O'Keefe, Choo, Richards 2013, [DOI](https://doi.org/10.1002/gcc.22078)); **PMID 35984507** (Carvalho *et al.* 2022, [DOI](https://doi.org/10.1007/s00018-022-04508-7)), which reports mitochondrial respiration in differentiated SH-SY5Y and **is read in this repository** (`reading_state.md`, two receipts). 🔴 **My prediction was too strong and I was too confident in a corpus-shaped negative.** See §5.1 — the refutation is also the most valuable result in this file |
| **P4** | 🟢 **SUPPORTED** | `Wwox AND (soleus OR "extensor digitorum" OR "fiber type" OR "muscle fiber")` → **4** records. One is the source itself (`PMID 30755385`); the other three are **two cattle-carcass GWAS** and **one paediatric mitochondrial NGS-panel report**, in none of which WWOX is more than a positional candidate gene in a list — **none reuses the fibre-type WWOX gradient**. 🔴 **Their identifiers are deliberately withheld here:** they are the negative half of a census, nothing in this file leans on them, and naming an unread paper inside a reasoning file is exactly the debt `legend_lint` counts. Repository half already measured: `soleus`/`soleo`/`EDL`/`slow-twitch` → **zero** hits outside the paper's own dossier. 🎯 **The one within-animal WWOX-abundance-versus-vulnerability gradient in this literature has been read by LEGEND and used by nobody, inside or outside** |
| **P5** | 🟢 **SUPPORTED** | The hepatocyte's resilience is **conditional, not absolute**. Under a high-fat-diet challenge the `Wwox^hep−/−` line reports **serum ALT ≈2× at 7 months** (`PMID 29724996`, `complete_fulltext_read`, `reading_state.md:97`; recorded at `analysis/peripheral_phenotype_denominator_audit_20260922.md:91` and `:164`). 🔴 **Consequence for the ladder, stated plainly: "L1/L2 tolerate" means "tolerate at baseline, on the endpoints measured".** The ladder is a ladder of *challenged and unchallenged states*, not of cell identities alone |
| **P6** | 🟢 **SUPPORTED**, with an unpredicted rider | `Wwox[tiab] AND (CreER[tiab] OR "tamoxifen-inducible"[tiab] OR "inducible deletion"[tiab] OR "inducible knockout"[tiab])` → **1** record, and it is **not** a two-age design. 🔴 **A first query was discarded before scoring, not after:** `Wwox AND (tamoxifen OR doxycycline OR inducible …)` returned **199** because `inducible` expanded to `induce/induced/inducing`; a wrong expansion is discarded, not counted. **Rider in §5.2** |
| **P7** | 🟢 **SUPPORTED — and it weakens `R1`, as I said in advance that it would** | `mechanism_intervention_map.md:308-313`, read directly: *"Human metabolism is normal, and it was checked four times"* — lactate, ammonia, acylcarnitines, a complete metabolic and mitochondrial screen including **muscle biopsy**, and **MRS**, all normal; and the single outlier is cerebral lactate *"extremely low"*, **the opposite of the Warburg prediction**, in a patient carrying a confounding HSPG2 variant (`DL-BIO-008`). 🔴 **This is a brain-compartment measurement and it runs against the metabolic reading**, which is why `FT-049` does not rescue it (§5.3) |

### 5.1 🎯 THE UNPREDICTED FINDING — the refutation of `P3` collapses `R1` and `R2` into one axis

🔴 **I did not predict this. It emerged while scoring `P3` and is recorded as an unpredicted finding,
not as a scored prediction.**

According to PubMed, **PMID 23765596** ([DOI](https://doi.org/10.1002/gcc.22078)) reports that
**the cell's metabolic state sets WWOX expression, not only the other way round**:

> *"altering metabolism from glycolysis to oxidative phosphorylation causes stable increase in
> steady-state levels of transcripts of the WWOX gene … exposure to hypoxic conditions, in which
> cells rely on glycolysis, causes a downregulation of WWOX mRNA"*
> — **🔴 abstract depth. Not read. See the reading debt in §5.1.1.**

And **PMID 26390919** ([DOI](https://doi.org/10.1002/gcc.22286)) places WWOX in a genetic
interaction with respiratory-complex deficiency that **requires its SDR active site**.

**What this does to §2, and it is not what I wanted.** `R1` (oxidative-dependence gating) and `R2`
(expression-dose gating) were written as **rivals**, and §2.1 recorded that soleus-versus-EDL could
not separate them. **If metabolic state drives WWOX transcription, they are not rivals — they are
one axis with an arrow in it:**

> **a compartment's oxidative setpoint sets how much WWOX it expresses; the compartments that
> express the most are the compartments whose loss is felt.** Soleus > EDL is then not a
> coincidence between two variables; it is the same variable measured twice.

🎯 **This is the only thing in this file that unifies rows rather than adding one.** It predicts the
ladder's shape from a single quantity — and it predicts, without being fitted to them, the two rows
I refused to build on: the **oligodendrocyte**, which is constitutively glycolytic and exports
lactate, and the **astrocyte**, likewise, should both sit at the resilient end. `L9` says they do.
🔴 **`L9` is second-hand and I do not count it as confirmation** — but it is the first time anything
in this repository has offered *any* explanation for the Olig2-Cre and GFAP-Cre negatives, which
until now were used only as evidence about the neuron.

#### 5.1.1 🔴 THE DEBT THIS FINDING CARRIES, AND THE REDISCOVERY IT PARTLY IS

**Reading debt — declared, and no conclusion rests on it.**

| PMID | LEGEND status, measured | What is permitted |
|---|---|---|
| **26390919** | `CORPUS-STUB-125` in `registries/paper_registry_current.md:1917-1925`, status **`not_processed`**; queue entry **`FT-006`** at `research/full_text_queue_current.md:94-101`, priority MED, surface **`absent`**, and at `:2962` **`unrecoverable_by_these_routes`**. **No read receipt. Abstract depth only** | Citable (registry-declared **and** queue-declared). 🔴 **UNDISCHARGED READING DEBT.** No conclusion in this file rests on it |
| **23765596** | Registry `:5583-5597`, **`screened — corpus placeholder`**, Tier C, `LIT-0374`, *"Role: background corpus only"*, **`Claim links: none`**. **No read receipt, no queue entry.** Also a **Drosophila/HEK293** system | Citable as a registry-declared record. 🔴 **UNDISCHARGED READING DEBT, and the weaker of the two.** No conclusion rests on it |

🔴 **And the honest grading, which costs this file its best line.** The *fact* is **not new to this
repository**. `analysis/adelaide_node_discriminator_20260921.md:249`, `:288` and `:329` already hold
*"Galactose / forced OXPHOS raising WWOX transcript in HEK293"* — **second-hand via a review, no
receipt, transcript-only, protein never reported** — and `next_node_scout_20260921_orchestrator.md:275`
already records the two questions it owes (*was protein measured; is the raised transcript the
full-length correctly spliced isoform*).

> **Grade: the ingredient is a `REDISCOVERY`; the use is not.** In every place the repository holds
> it, the fact is filed as a **candidate therapeutic lever for raising WWOX** — and killed there,
> because the reference genotype class has nothing functional to upregulate. **Nowhere is it turned
> around and used as a rule predicting which compartment fails.** That inversion, and its match to
> the unused `L5` gradient, is this file's contribution. It is a connection, not a discovery, and it
> is graded as one.

### 5.2 The rider on `P6` — the decisive reagent for `R6` already exists in this field

`PMID 36572673` (Husanie *et al.* 2022) is a **tamoxifen-inducible conditional `Wwox`** mouse study,
**read in full by LEGEND** (`research/fulltext_dossiers/PMID36572673.md`, `complete_fulltext_read`,
PMC9792466, [DOI](https://doi.org/10.1038/s41419-022-05519-9)), in **pancreatic acinar** tissue for an
oncological question. 🔴 **It is not a two-age design and it is not a neural or metabolic phenotype —
it must not be pooled with any row of §1.** What it establishes is narrower and still useful:
**an inducible `Wwox` deletion system exists and has been used**, so `R6`'s decisive experiment —
delete in one compartment at two ages — is a **cross and a cohort**, not a new allele. That moves its
executability class and nothing else.

🎯 **It also adds a row I did not have.** *Pancreatic acinar tissue, adult inducible deletion*:
WWOX loss there is reported to **accelerate tumour development in a cancer-driver context**, not to
produce a spontaneous phenotype on its own — consistent with the ladder's resilient end, and
consistent with `P5`'s lesson that resilience is **conditional on challenge**. Recorded as an
observation, not scored.

### 5.3 🔴 Why `FT-049` does NOT rescue node `G1`, although it looks as though it should

**The argument I expected to be able to make, and cannot.** `FT-049` says a phenotype measured in
blood does not identify the tissue where the lesion sits. Node **`G1`** of
`wwox_independent_downstream_rescue_20260922.md:103` — HIF1α/PDK1/glycolytic shift — was scored down
partly on *"human metabolism is normal, and it was checked four times"*. If those four screens are
**serum** screens, `FT-049` would say they cannot exclude a compartment-restricted lesion, and `G1`
would be under-scored.

🔴 **It does not work, and `P7` is why.** The four screens are **not all serum**: they include a
**muscle biopsy** and an **MRS**, and the MRS is a *brain-compartment* measurement that came back in
the **wrong direction** for the Warburg reading (`mechanism_intervention_map.md:308-313`). A
compartment-restricted rescue of `G1` needs the compartment to be unmeasured; **the two compartments
this node most implicates — oxidative muscle and brain — are precisely the two that were measured.**

> **`G1` stays where `wwox_independent_downstream_rescue_20260922.md` put it.** It is not re-scored,
> not reopened and not re-proposed here. The one thing I add is the **reason**: `G1`'s problem is not
> that it was measured in the wrong compartment — it is that it was measured in the right one.

---

## 6 · THE MINIMAL DISCRIMINATING EXPERIMENT

**Live hypotheses after §5:** `R1⊕R2` (merged — the **metabolic-setpoint axis**), `R3`, `R4`, `R5`,
`R6`.

**Design rule applied:** every component must own a hypothesis **pair** that nothing cheaper
separates. Components owning no pair are **cut**, and the blind spot each cut creates is stated.

| # | Component | The pair it separates that nothing cheaper separates | Executability |
|---|---|---|---|
| **E1** | **The per-Cre-line endpoint matrix.** For every WWOX conditional line in the corpus — Alb-Cre, adipocyte-Cre, ACTA1-rtTA, Synapsin-Cre, Nestin-Cre, Olig2-Cre, GFAP-Cre, BK5-Cre, EIIA-Cre, the inducible pancreatic line — record **which endpoints were run, with what n, what comparator, and at what Cre-onset age**, from the dossiers and deepdive manifests already on disk | 🎯 **`R5` versus everything, and half of `R6`.** Nothing else can establish that there is an explanandum at all. 🔴 **This is a gate, not the product** — it is here because the node is worthless if the ladder is an artefact of unequal panels, and that is the cheapest possible way to find out | 🟢 **EXECUTABLE NOW.** Zero cost, no animal, no reagent, no fetch, no external contact. Material is local |
| **E2** | 🎯 **Fibre-type-resolved analysis in the existing `Wwox^ΔSKM` line.** In one section set: WWOX immunolocalisation + **oxidative-enzyme histochemistry (SDH/COX)** + myosin-heavy-chain fibre typing + an atrophy/lesion index — across soleus, EDL **and the deep-versus-superficial regions of one gastrocnemius**, where oxidative character varies within a single muscle | 🎯 **`R1` versus `R2` — and nothing else can separate them.** §2.1 recorded that soleus/EDL cannot, because both variables move together there; the deep/superficial gradient is the cheapest place they come apart. 🔴 **And it kills `R5` and `R6` by construction for these rows** — one animal, one driver, one onset, one panel, so unequal endpoints and unequal Cre timing cannot explain a within-section gradient | 🟡 **MINOR ADAPTATION.** Reagents: SDH/COX histochemistry and MyHC typing are routine; the WWOX antibody used in this model is on record. Gated on banked or colony `Wwox^ΔSKM` muscle — 🔴 **a question this file was not permitted to ask** |
| **E3** | **Cell-type-resolved WWOX protein in the WILD-TYPE brain**, co-stained with an oxidative marker: neuron versus oligodendrocyte versus astrocyte, with a regional axis | 🎯 **`R2` versus `R4`, in the compartment that matters** — `R2` predicts WWOX abundance tracks the oxidative marker and the ladder; `R4` predicts abundance is flat while the **partner** set varies. It is also the **only** component that tests whether the muscle rule transfers to brain at all. 🔴 **No knockout is needed and no disease animal is used — this is wild-type tissue** | 🟡 **MINOR ADAPTATION.** An N-terminal anti-WWOX antibody with a catalogued immunogen and rodent identity is already inventoried in `wwox_antibody_epitope_census_20260922.md`; markers are standard. No new allele, no new colony |
| **E4** | **Two-age induction in one compartment**, using an inducible `Wwox` conditional system crossed to a single non-pancreatic driver | 🎯 **`R6` versus everything.** The only design in which cell type is held constant and onset varies. §5.2 shows the allele and the induction system exist | 🔴 **NEW PROGRAM.** A new cross, a new cohort and a new phenotyping plan. Listed because `R6` is otherwise unfalsifiable, **not** because it should be run first |

### 6.1 What I cut, and the blind spot each cut creates

| Cut | Why | 🔴 Blind spot created |
|---|---|---|
| **`R3`'s regeneration-blockade arm** (block hepatocyte renewal and look for an unmasked phenotype) | Owns only `R3`, and `R3` is already weakened by `L4` — the failing myofibre failed with a **transcriptional/metabolic** signature, not a degenerative one | 🔴 **Cannot exclude** that hepatocyte resilience is renewal-dependent. If `E1` shows the resilient lines were given the same panels as the vulnerable ones — i.e. `R5` falls — this cut becomes the bottleneck and `R3` returns |
| **Respirometry / OCR:ECAR in donor-derived cells** | 🔴 **It is not mine.** `mechanism_intervention_map.md:513` already names Seahorse on donor-derived fibroblasts/LCL, and on the existing WWOX-KO organoids, as its `DECISIVE_PRECLINICAL_TEST`. I do not re-propose, rename or claim any part of it | Loses the direct flux measurement. `E2` substitutes an **enzyme-histochemical surrogate**, which is anatomical rather than quantitative |
| **Acquiring `PMID 33914858`, `26390919` or `23765596`** | 🔴 **Out of scope for this act** — no acquisition was attempted and no external contact was made. These are the node's reading debts, declared in §1.1 and §5.1.1, and they are named as debts rather than converted into experiments | The `L8`/`L9` rows and the §5.1 arrow stay second-hand. **The node is built so that it survives without them, and it is sharper with them** |
| 🔴 **Every pharmacological arm, of every kind** | **Out of scope by construction.** No molecule, class, dose, route or compound screen is named anywhere in this file | None. A mechanistic probe is not supposed to carry one |

### 6.2 Executability verdict

| Check | Answer |
|---|---|
| Reagent exists? | 🟢 Yes for E1–E3 — SDH/COX histochemistry, MyHC typing, a catalogued anti-WWOX antibody, standard cell-type markers. 🔴 E4 needs a new cross |
| Sample exists? | 🟢 E1: local files. 🟡 E2: **the decisive unknown** — banked or colony `Wwox^ΔSKM` muscle; **not asked**. 🟢 E3: wild-type rodent brain. 🔴 E4: does not exist |
| Technique exists? | 🟢 Yes — none of E1–E3 is beyond routine histology |
| Readout interpretable? | 🟢 E1, E2, E3. 🟡 E4 only with a littermate-matched, age-matched denominator |
| Comparator exists? | 🟢 E1–E3 — littermate controls and, for E2, the animal's own contralateral and within-section gradient |

> **CLASS: 🟢 EXECUTABLE NOW (E1) · 🟡 MINOR ADAPTATION (E2, E3) · 🔴 NEW PROGRAM (E4).**
> **Overall: MINOR ADAPTATION, gated on one tissue question this file was not permitted to ask.**
> 🎯 **E1 is executable today at zero cost and can kill the whole node. It is the correct first
> move, and I would rather it killed the node cheaply than that the node survived expensively.**

---

## 7 · VALUE — the three-part test, answered honestly

| Requirement | Status |
|---|---|
| **Mechanistic bridge** | 🟡 **PARTIAL, and weaker than it reads.** The metabolic-setpoint arrow (§5.1) is supported by **two abstract-depth, unread, registry-declared records** and by **one unused first-hand datum** (`L5`). The fact itself is already held second-hand in the repository and is graded a **`REDISCOVERY` of the ingredient**. It is `IPOTESI`, not `DATO`, and it is not promoted |
| **Disease-relevant endpoint** | 🔴 **FAILS TODAY.** The ladder's strongest, first-hand rows are **skeletal muscle and liver**, not brain. The brain limb is `E3` and is untested. And `P7` — which I preregistered **against myself** — confirms that the held human evidence, including a **brain** MRS, runs **against** the metabolic reading |
| **Discriminating experiment** | 🟢 **PRESENT.** §6 separates five hypotheses with four components, one of which is free and can kill the node |

### 7.1 🔴 THE WWOX-INDEPENDENT RESCUE TEST — run in full, and it FAILS

The brief requires **all four** links or an explicit failure. Run honestly:

| Link | Status |
|---|---|
| **WWOX LOSS** | 🟢 Present — eight conditional lines, §1 |
| **→ plausible downstream mechanism** | 🟡 Present but `IPOTESI` — the metabolic-setpoint axis, §5.1, on two unread records |
| **→ intervention POINT** | 🔴 **FAILS.** Any intervention on fuel strategy lands on **`G1`/`R-05`/`N-08`**, which this repository has already scored down and **DEPRIORITIZED** (`mechanism_intervention_map.md:774`), and §5.3 shows `FT-049` does **not** rescue them. 🔴 **I name no molecule, no class, no dose and no route, and I do not propose neuroprotection of any kind** |
| **→ measurable disease-relevant ENDPOINT** | 🔴 **FAILS for the disease.** The measurable endpoints of this node are histological and muscular. A disease-relevant endpoint requires `E3` first |

> # 🔴 VERDICT: NOT YET ACTIONABLE
> **Two of three value requirements fail, and the four-part rescue test fails at two of four links.**
> This node is a **mechanistic and predictive probe**, not a therapeutic direction. Nothing in it may
> be read as one. **Nothing here is medical advice.**

### 7.2 What survives if the reading debts are never discharged

Scored twice, as §1.1 promised — the node **without** `L8` and `L9`, i.e. using only first-hand,
receipt-backed material:

| Holds without L8/L9 | Because |
|---|---|
| The ladder's **first-hand** core — L1, L2, L3, L4, L5, L6, L7, L10 | Every one carries a read receipt or is quoted from a receipted dossier with file and line |
| **`FT-049` is undeveloped, and the experiment it demands has never been designed** | Measured across the repository, not asserted |
| **`L5` and `L6` are unused, in this repository and in the literature** | `P4`, plus a zero-hit repository grep |
| **`P5` — resilience is conditional on challenge, not absolute** | From a paper read in full |
| **`E1`, `E2`, `E3`** | None of them needs `L8` or `L9` to be interpretable |
| ❌ **Lost without them** | The oligodendrocyte and astrocyte predictions of §5.1 — which is exactly why they are written as a *match*, never as confirmation |

---

## 8 · WHAT I COULD NOT VERIFY

1. 🔴 **`PMID 33914858` was not fetched and has no read receipt.** Rows `L8`/`L9` are second-hand
   (§1.1). Nothing rests on them.
2. 🔴 **`PMID 26390919` and `PMID 23765596` were not fetched.** Abstract depth only, via PubMed.
   `FT-006` records `26390919` as `unrecoverable_by_these_routes`. Nothing rests on them (§5.1.1).
3. 🔴 **No primary in §1 was re-fetched in this act.** `L2`–`L6` are 🔴 **SIBLING-ATTESTED** from
   LEGEND's own receipt-backed dossiers, with repository file and line at every use.
4. 🔴 **No figure panel was inspected by me.** `L5` is a dossier's pixel-level reading of Fig. S4.
5. 🔴 **Whether banked `Wwox^ΔSKM` muscle exists.** No external contact was made; the question is
   unasked, and `E2` is gated on it.
6. ⚪ **`R4` is untested in every direction.** No partner-availability data was sought in this act.
7. 🔴 **Whether any of this transfers to a human WWOX-DEE genotype class.** The ladder is built from
   **mouse conditional alleles**. It is not pooled with the rat `lde/lde`, with human WOREE or with
   human SCAR12, and no transfer is asserted.

---

## 9 · SOURCE ATTRIBUTION

🔵 Bibliographic records, query counts and abstracts in §5 were retrieved from **PubMed**. Articles
referenced there: PMID 26390919 ([DOI](https://doi.org/10.1002/gcc.22286)), PMID 23765596
([DOI](https://doi.org/10.1002/gcc.22078)), PMID 35984507 ([DOI](https://doi.org/10.1007/s00018-022-04508-7)),
PMID 36572673 ([DOI](https://doi.org/10.1038/s41419-022-05519-9)). The three
incidental records that form the negative half of the `P4` census are **deliberately not named**:
nothing leans on them and they were not read.

Repository sources, all quoted with file and line and labelled at every use: `PMID 24871327`
(receipt `FTR-20260810-24871327-01`), `PMID 30755385` (`complete_fulltext_read`), `PMID 34747138`
(receipt `FTR-20260810-34747138-01`), `PMID 29724996` (`complete_fulltext_read`), `PMID 34634460`
(via `CLAIM 021`), `PMID 33914858` (via `PAPER 004` / `CLAIM 003`, **second-hand**).

No new external source was retrieved beyond PubMed metadata, **no external contact was made**, no
canonical file was modified, no git command was run, no receipt was claimed and no commit candidate
was opened. No contact detail of any living person is reproduced.

🔴 **Nothing in this file is medical advice, and no molecule, class, dose, route or schedule is
named anywhere in it.**

---

# ORCHESTRATOR VERIFICATION — 2026-09-22

## V0 · 🔴 A defect in THIS repository's handling of this file, owned before anything else

Commit `51dacbe` captured this file **mid-write at 261 lines** and landed it on `main`. That was
the Orchestrator's error, not the Scientist's: `git add -A` was used to stage a sibling's commit
while this actor was still writing. The Scientist noticed independently and said so.

🎯 **It is the fifth member of the session's search-defect family, and the first to write to
canonical history rather than to produce a wrong number.** The shared question — *what objects were
eligible to match?* — applies to `git add -A` exactly as it applies to `grep`, `pgrep` and
`ls | grep`. The staging matcher's eligible set silently included a file the Orchestrator had
explicitly decided not to commit.

**Not repaired by history rewrite** (RESERVED, §21d; the partial is already published). Repaired
**forward**: this commit supersedes the truncated version with the complete 496-line file, staged by
**explicit path**. Standing correction: while any Scientist is running, stage by path, never `-A`.

## V1 · 🟢 Citation hygiene verified — no `UNREAD_PREMISE` exposure

Both new PMIDs are registry-declared (`23765596` 6 files; `26390919` 6 files + 3 queue hits), and
both are carried as **`UNDISCHARGED READING DEBT` with no conclusion resting on them.** LINT `PASS`,
growth anchors `PASS`. The gate that blocked this actor's previous node did not fire.

## V2 · 🎯 The self-grading is CORRECT, and it is the best thing in the file

C graded its own headline ingredient a **`REDISCOVERY`** and claimed only the inversion. Verified at
source — `adelaide_node_discriminator_20260921.md:249` holds:

> *"**Galactose / forced OXPHOS raising WWOX transcript** in HEK293 | `23765596`, second-hand via
> review — no receipt"*

…and `:288` **kills it**, as a therapeutic lever: *"nothing to upregulate … potentially adverse —
more transcript from a splice-defective allele."*

🔴 **So the fact was held, and held as a dead end. What is new is the direction of the arrow.** The
prior file asked *"can we raise WWOX?"* and answered no. This one asks *"does metabolic state set
WWOX expression, and does that predict which compartments fail?"* — the same datum, inverted from a
**therapeutic lever** into a **vulnerability rule**.

If it survives, it is the **first explanation this repository has offered for the Olig2-Cre /
GFAP-Cre negatives**: the resilient end would contain the glycolytic oligodendrocyte and astrocyte.
🔴 It rests on two **unread** records and stays `IPOTESI`.

## V3 · Two disciplines worth carrying forward

**P3 was REFUTED against its author** — C predicted no respiration had been measured in any WWOX
system; 3 of 4 hits do exactly that, and the refutation is what produced the node's central idea.
This is now the second time this session that a **pre-registered prediction failing** was worth more
than it succeeding.

**The instrument defect was measured, not assumed.** `Wwox AND (conditional OR floxed OR Cre) AND
(knockout OR deletion)` returns **10 records and omits every conditional line this node is built
on**, against a positive control of **99**. Therefore **every negative in the file is explicitly an
upper bound** — the query was characterised before its zeros were trusted, which is the
search-defect discipline applied prospectively rather than after a failure.

## V4 · The negative that was kept

C expected `FT-049` to show node `G1` under-scored on a blood-compartment negative. It does not: the
human screens include a **muscle biopsy and an MRS**, and the MRS is a brain measurement in the
wrong direction. 🔴 **`G1`'s problem is that it was measured in the *right* compartment.** `G1` is
**not** re-scored, reopened or re-proposed — a refuted expectation recorded without being converted
into a reason to reopen something.

## V5 · Verdict on the node

**`NOT YET ACTIONABLE`**, and correctly so: the four-part WWOX-independent rescue test was run in
full and **fails at two of four links** — the disease-relevant endpoint fails because the ladder's
first-hand rows are muscle and liver while `P7` runs against the brain limb, and the intervention
point lands on already-deprioritised nodes.

**What is genuinely new and cheap:** `E1`, a per-Cre-line endpoint matrix built from local files
only — 🟢 **`EXECUTABLE NOW`, zero cost** — which tests `R5` (*"there is no ladder; the negatives are
endpoint-limited"*) before any of the ladder's biology is believed. **That is the right first move:
it asks whether the explanandum exists before explaining it** — the same discipline that made "count
the vacuoles first" the right answer on the previous node.
